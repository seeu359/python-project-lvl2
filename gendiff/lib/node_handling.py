from gendiff.lib import data_handling as dh


def format_child(node1, node2):
    result = []
    child_list = dh.get_sorted_keys(node1, node2)
    for child in child_list:
        if child in node1 and child in node2:
            if isinstance(node1.get(child), dict) and \
                    isinstance(node2.get(child), dict):
                result.append({'key': child,
                               'type': 'parent',
                               'state': dh.STATE_NO_CHANGE,
                               'children': format_child(node1.get(child),
                                                        node2.get(child))
                               })
            else:
                result.append(compare_values(node1, node2, child))
        elif child in node1 or child in node2:
            node = dh.get_find_node(node1, node2, child)
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
                'state': dh.STATE_NO_CHANGE,
                'value': node1.get(child),
                }
    else:
        return {'key': child,
                'type': 'children',
                'state': dh.STATE_CHANGE,
                'old_value': node1.get(child),
                'new_value': node2.get(child),
                }


def flat_structure_process(root, node):
    return {'key': root,
            'type': 'children',
            'state': node[1],
            'value': node[0].get(root),
            }
