from gendiff.lib import data_handling

NOT_CHANGED = '='
OLD_KEY_VALUES = ('REP-', '-')
UPDATED_KEY_VALUES = ('REP+', '+')
NOT_FORMAT = 'NoAction'


def format_parent(node1, node2, parent):
    result = dict()
    keys_list = data_handling.get_sorted_keys(node1, node2)
    for key in keys_list:
        if key in node1 and key in node2:
            if not isinstance(node1.get(key), dict) and not \
                    isinstance(node2.get(key), dict):
                value = format_child(node1, node2, key, parent)
                result.update(value)
            elif isinstance(node1.get(key), dict) and \
                    isinstance(node2.get(key), dict):
                result[key] = [format_parent(node1.get(key),
                                             node2.get(key),
                                             f'{parent}.{key}'),
                               NOT_CHANGED,
                               parent]
            else:
                value = comprehensive_format(node1, node2, key, parent)
                result.update(value)
        else:
            result[key] = single_node_process(data_handling.define_node
                                              (node1, node2, key),
                                              parent, key)
    return result


def format_child(parent1, parent2, key, parent):
    result = dict()
    if parent1[key] == parent2[key]:
        result[key] = [parent1.get(key), NOT_CHANGED, parent]
        return result
    elif parent1[key] != parent2[key]:
        result[f'{OLD_KEY_VALUES[0]}{key}'] = [parent1.get(key),
                                               OLD_KEY_VALUES[1], parent]
        result[f'{UPDATED_KEY_VALUES[0]}{key}'] = [parent2.get(key),
                                                   UPDATED_KEY_VALUES[1],
                                                   parent]
        return result


def comprehensive_format(parent1, parent2, key, parent):
    result = dict()
    if isinstance(parent1.get(key), dict) and not \
            isinstance(parent2.get(key), dict):
        result[f'{OLD_KEY_VALUES[0]}{key}'] = [process_without_format
                                               (parent1.get(key),
                                                f'{parent}.{key}'),
                                               OLD_KEY_VALUES[1], parent]
        result[f'{UPDATED_KEY_VALUES[0]}{key}'] = [parent2.get(key),
                                                   UPDATED_KEY_VALUES[1],
                                                   parent]
        return result
    elif not isinstance(parent1.get(key), dict) and \
            isinstance(parent2.get(key), dict):
        result[f'{OLD_KEY_VALUES[0]}{key}'] = [parent1.get(key),
                                               OLD_KEY_VALUES[1], parent]
        result[f'{UPDATED_KEY_VALUES[0]}{key}'] = [process_without_format
                                                   (parent2.get(key),
                                                    f'{parent}.{key}'),
                                                   UPDATED_KEY_VALUES[1],
                                                   parent]
        return result


def process_without_format(node, parent):
    result = dict()
    keys_list = data_handling.get_sorted_keys(node)
    for key in keys_list:
        if not isinstance(node.get(key), dict):
            result[key] = ([node.get(key), NOT_FORMAT, parent])
        elif isinstance(node.get(key), dict):
            result[key] = [process_without_format(node.get(key),
                                                  f'{parent}.{key}'),
                           NOT_FORMAT, parent]
    return result


def single_node_process(node, parent, key):
    if not isinstance(node[0].get(key), dict):
        return [node[0].get(key), node[1], parent]
    elif isinstance(node[0].get(key), dict):
        result = [process_without_format(node[0].get(key),
                                         f'{parent}.{key}'), node[1],
                  parent]
        return result
