from gendiff.formatters.formatter_data import data_handling as dh

ADDED = 'was added with value:'
REMOVED = 'was removed'
UPDATED = 'was updated. From'
COMPLEX = '[complex value]'


def format_root(data, result, path):
    for node in data:
        if node['type'] == 'children':
            result.append(format_child(node, path))
        if node['type'] == 'parent' and node['state'] == dh.STATE_NO_CHANGE:
            format_root(node['children'], result, path + f"{node['key']}.")
        elif node['type'] == 'parent' and node['state'] == dh.STATE_ADDED:
            result.append(f"Property '{path}{node['key']}' "
                          f"{ADDED} {COMPLEX}\n")
        elif node['type'] == 'parent' and node['state'] == dh.STATE_REMOTE:
            result.append(f"Property '{path}{node['key']}' {REMOVED}\n")

    return ''.join(result).strip()


def format_child(node, path):
    """
    Takes control if the previous value is not a parent node. Returns a string
    representation of the changed key with the path from the parent node.
    :param node: type(data) == dict. Node, where doing format
    :param path: type(path) == str. Path from parent's node to our key
    :return: type == str
    """
    if node['state'] == dh.STATE_ADDED:
        return f"Property '{path}{node['key']}' {ADDED} " \
               f"{dh.format_reduction(node['value'], 'plain')}\n"
    elif node['state'] == dh.STATE_REMOTE:
        return f"Property '{path}{node['key']}' {REMOVED}\n"
    elif node['state'] == dh.STATE_CHANGE:
        return f"Property '{path}{node['key']}' {UPDATED} " \
               f"{dh.format_reduction(node['old_value'], 'plain')} to " \
               f"{dh.format_reduction(node['new_value'], 'plain')}\n"
    else:
        return ''
