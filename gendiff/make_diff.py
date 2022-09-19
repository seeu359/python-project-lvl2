from collections import ChainMap
from gendiff import constants as const

DEFAULT_VALUE = 'default_value_for_the_missing_key'


def make_diff(file1_data, file2_data):
    """
    :param file1_data: type(file1_data) is dict
    :param file2_data: type(file2_data) is dict
    :return: type list
    """
    result = []
    keys_list = get_sorted_keys(file1_data, file2_data)
    for key in keys_list:
        file1_key = file1_data.get(key, DEFAULT_VALUE)
        file2_key = file2_data.get(key, DEFAULT_VALUE)
        if file1_key is not DEFAULT_VALUE and file2_key is not DEFAULT_VALUE:
            if isinstance(file1_key, dict) and isinstance(file2_key, dict):
                result.append({const.KEY: key,
                               const.TYPE: const.TYPE_PARENT,
                               const.STATE: const.STATE_NO_CHANGED,
                               const.CHILDREN: make_diff(file1_key,
                                                         file2_key)
                               })
            else:
                result.append(compare_values(file1_data, file2_data, key))
        elif file1_key is not DEFAULT_VALUE:
            node_type, format_key = (const.TYPE_PARENT, const.CHILDREN) if \
                isinstance(file1_key, dict) else (const.TYPE_CHILDREN,
                                                  const.VALUE)
            result.append({const.KEY: key,
                           const.TYPE: node_type,
                           const.STATE: const.STATE_REMOVED,
                           format_key: file1_key
                           })
        elif file2_key is not DEFAULT_VALUE:
            node_type, format_key = (const.TYPE_PARENT, const.CHILDREN) if \
                isinstance(file2_key, dict) else (const.TYPE_CHILDREN,
                                                  const.VALUE)
            result.append({const.KEY: key,
                           const.TYPE: node_type,
                           const.STATE: const.STATE_ADDED,
                           format_key: file2_key
                           })
    return result


def get_sorted_keys(*parents):
    keys_list = list(ChainMap(*parents))
    keys_list.sort()
    return keys_list


def compare_values(node1, node2, child):
    if node1.get(child) == node2.get(child):
        return {const.KEY: child,
                const.TYPE: const.TYPE_CHILDREN,
                const.STATE: const.STATE_NO_CHANGED,
                const.VALUE: node1.get(child),
                }
    else:
        return {const.KEY: child,
                const.TYPE: const.TYPE_CHILDREN,
                const.STATE: const.STATE_CHANGED,
                const.OLD_VALUE: node1.get(child),
                const.NEW_VALUE: node2.get(child),
                }
