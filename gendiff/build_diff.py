from collections import ChainMap


STATE_NO_CHANGE = 'no change'
STATE_CHANGE = 'changed'
STATE_REMOTE = 'removed'
STATE_ADDED = 'added'


def make_diff(file1_data, file2_data):
    """
    :param file1_data: type(file1_data) is dict
    :param file2_data: type(file2_data) is dict
    :return: type list
    """
    result = []
    keys_list = get_sorted_keys(file1_data, file2_data)
    for root in keys_list:
        if root in file1_data and root in file2_data:
            if (isinstance(file1_data[root], dict) and isinstance(
                    file2_data[root], dict)):
                result.append({'key': root,
                              'type': 'parent',
                               'state': STATE_NO_CHANGE,
                               'children': format_child(file1_data.get(root),
                                                        file2_data.get(root))
                               })
                continue
            else:
                result.append(compare_values(file1_data, file2_data, root))
                continue
        elif root in file1_data or root in file2_data:
            node = get_find_node(file1_data, file2_data, root)
            if isinstance(node[0].get(root), dict):
                result.append({'key': root,
                              'type': 'parent',
                               'state': node[1],
                               'children': node[0].get(root)
                               })
            else:
                result.append(flat_structure_process(root, node))
    return result


def get_sorted_keys(*parents):
    keys_list = list(ChainMap(*parents))
    keys_list.sort()
    return keys_list


def format_child(node1, node2):
    """
    :param node1: type(node1) == dict
    :param node2: type(node2) == dict.
    :return:
    """
    result = []
    child_list = get_sorted_keys(node1, node2)
    for child in child_list:
        if child in node1 and child in node2:
            if isinstance(node1[child], dict) and isinstance(node2[child],
                                                             dict):
                result.append({'key': child,
                               'type': 'parent',
                               'state': STATE_NO_CHANGE,
                               'children': format_child(node1.get(child),
                                                        node2.get(child))
                               })
                continue
            else:
                result.append(compare_values(node1, node2, child))
                continue
        elif child in node1 or child in node2:
            node = get_find_node(node1, node2, child)
            node_type, value = ('parent', 'children') if \
                isinstance(node[0][child], dict) else ('children', 'value')
            result.append({'key': child,
                           'type': node_type,
                           'state': node[1],
                           value: node[0].get(child),
                           })
    return result


def compare_values(node1, node2, child):
    if node1.get(child) == node2.get(child):
        return {'key': child,
                'type': 'children',
                'state': STATE_NO_CHANGE,
                'value': node1.get(child),
                }
    else:
        return {'key': child,
                'type': 'children',
                'state': STATE_CHANGE,
                'old_value': node1.get(child),
                'new_value': node2.get(child),
                }


def flat_structure_process(root, node):
    return {'key': root,
            'type': 'children',
            'state': node[1],
            'value': node[0].get(root),
            }


def get_find_node(node1, node2, child):
    if child in node1:
        return node1, STATE_REMOTE
    else:
        return node2, STATE_ADDED
