from collections import ChainMap


STATE_NO_CHANGED = 'no change'
STATE_CHANGED = 'changed'
STATE_REMOVED = 'removed'
STATE_ADDED = 'added'


def make_diff(file1_data, file2_data):
    """
    :param file1_data: type(file1_data) is dict
    :param file2_data: type(file2_data) is dict
    :return: type list
    """
    result = []
    keys_list = get_sorted_keys(file1_data, file2_data)
    for key in keys_list:
        if key in file1_data and key in file2_data:
            if (isinstance(file1_data[key], dict) and isinstance
               (file2_data[key], dict)):
                result.append({'key': key,
                               'type': 'parent',
                               'state': STATE_NO_CHANGED,
                               'children': make_diff(file1_data.get(key),
                                                     file2_data.get(key))
                               })
                continue
            else:
                result.append(compare_values(file1_data, file2_data, key))
                continue
        elif key in file1_data or key in file2_data:
            node, state = get_find_node(file1_data, file2_data, key)
            node_type, format_key = ('parent', 'children') if \
                isinstance(node[key], dict) else ('children', 'value')
            result.append({'key': key,
                           'type': node_type,
                           'state': state,
                           format_key: node[key]
                           })
    return result


def get_sorted_keys(*parents):
    keys_list = list(ChainMap(*parents))
    keys_list.sort()
    return keys_list


def compare_values(node1, node2, child):
    if node1.get(child) == node2.get(child):
        return {'key': child,
                'type': 'children',
                'state': STATE_NO_CHANGED,
                'value': node1.get(child),
                }
    else:
        return {'key': child,
                'type': 'children',
                'state': STATE_CHANGED,
                'old_value': node1.get(child),
                'new_value': node2.get(child),
                }


def get_find_node(node1, node2, child):
    if child in node1:
        return node1, STATE_REMOVED
    else:
        return node2, STATE_ADDED
