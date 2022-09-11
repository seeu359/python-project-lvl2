"""
This formatter display difference between 2 files as:
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to [complex value]
"""

from gendiff import build_diff as bd
from gendiff.formatters import value_handling as vh

ADDED = 'was added with value:'
REMOVED = 'was removed'
UPDATED = 'was updated. From'
COMPLEX = '[complex value]'


def format_diff(diff):
    return format_root(diff, [], '')


def format_root(diff, result, path):
    """
    Processes the root node and passes control to process the children
    :param diff: type(introduction) == dict. Internal representation
    from diff
    :param result: type(result) == list. Intermediate result.
    :param path: type(path) == str. Intermediate path to the changed node
    :return: type str
    """
    for node in diff:
        if node['type'] == 'children':
            result.append(format_child(node, path))
        if node['type'] == 'parent' and node['state'] == bd.STATE_NO_CHANGED:
            format_root(node['children'], result, f"{path}{node['key']}.")
        elif node['type'] == 'parent' and node['state'] == bd.STATE_ADDED:
            result.append(f"Property '{path}{node['key']}' "
                          f"{ADDED} {COMPLEX}\n")
        elif node['type'] == 'parent' and node['state'] == bd.STATE_REMOVED:
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
    if node['state'] == bd.STATE_ADDED:
        return f"Property '{path}{node['key']}' {ADDED} " \
               f"{format_specific_value(node['value'])}\n"
    elif node['state'] == bd.STATE_REMOVED:
        return f"Property '{path}{node['key']}' {REMOVED}\n"
    elif node['state'] == bd.STATE_CHANGED:
        return f"Property '{path}{node['key']}' {UPDATED} " \
               f"{format_specific_value(node['old_value'])} to " \
               f"{format_specific_value(node['new_value'])}\n"
    else:
        return ''


def format_specific_value(value):
    """
        :param value: type(value) == str
        :return: type str
    """
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{str(value)}'"
    else:
        return vh.format_value(value)
