"""
Default formatter.
This formatter display difference between 2 files as:
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: {
            key: value
        }
}
"""
from gendiff.formatters import value_handling as vh
from gendiff import build_diff as bd

MARK = {'removed': ('- ', 2),
        'added': ('+ ', 2),
        'no change': ('', 0),
        }
INDENT_STEP = 4
CORRECT_INDENT = 2


def format_diff(diff):
    return format_root(diff, ['{\n'], INDENT_STEP)


def format_root(diff, result, indent):
    """
    The function, depending on the type of node, passes control to the handler
    functions
    :param diff: type(introduction) == dict. Takes an internal
    representation from the
    diff
    :param result: type(result) == list. Intermediate result.
    :param indent: type(indent) == dict. Default indent == 4
    :return: type(str)
    """
    for data in diff:
        if data['type'] == 'parent' and data['state'] != bd.STATE_NO_CHANGED:
            result.append(format_parent(data, indent))
        if data['type'] == 'parent' and data['state'] == bd.STATE_NO_CHANGED:
            result.append(format_parent(data, indent))
            format_root(data.get('children'),
                        result, indent + INDENT_STEP)
        elif data['type'] == 'children':
            result.append(format_child(data, indent))
    result.append(' ' * (indent - INDENT_STEP) + '}\n')
    return ''.join(result).strip()


def format_parent(node, indent):
    """
    Takes control from the parent. The difference is displayed as one of the
    characters before the key.The '+' sign indicates that the node was added
    in the second file. Sign '-' that the node was deleted in the second file.
    The absence of a sign in front of the parent means that its internal
    structure has changed
    :param node: type(node) == dict
    :param indent: type(indent) == int
    :return: type str
    """
    if node['state'] == bd.STATE_NO_CHANGED:
        return f"{' ' * indent}{node['key']}: {{\n"
    else:
        margin = f"{' ' * (indent - MARK[node['state']][1])}"
        return f"{margin}{MARK[node['state']][0]}{node['key']}: {{" \
               f"{alocate_value(node['children'], indent)}\n"


def alocate_value(node, indent):
    if isinstance(node, dict):
        return nested_format(node, indent + INDENT_STEP)
    else:
        return format_specific_value(node)


def format_child(node, indent):
    """
    Takes control if key value is not a dictionary. Returns a key preceded by a
    key character that indicates changes made to the given key.
    If in front of the key '+': Key was added in second file
    If '-': Key was removed in second file
    If no symbols before the key: key values was not changed
    If the names of two neighboring keys are the same, key values was changed in
    second file.
    :param node: type(node) == dict
    :param indent: type(indent) == int
    :return: type str
    """
    result = ''
    if node['state'] == bd.STATE_CHANGED:
        bracket = '{' if isinstance(node['old_value'], dict) else ''
        result += f"{' ' * (indent - CORRECT_INDENT)}- {node['key']}: " \
                  f"{bracket}{alocate_value(node['old_value'], indent)}\n"
        bracket = '{' if isinstance(node['new_value'], dict) else ''
        result += f"{' ' * (indent - CORRECT_INDENT)}+ {node['key']}: " \
                  f"{bracket}{(alocate_value(node['new_value'], indent))}\n"
    else:
        mark, make_indent = MARK[node['state']]
        margin = ' ' * (indent - make_indent)
        result += f"{margin}{mark}{node['key']}: " \
                  f"{(format_specific_value(node['value']))}\n"
    return result


def nested_format(node, indent):
    """
    Function that comprehensively handles a remote or added parent node with
    all children
    :param node: type(node) == dict.
    :param indent: type(indents) == int.
    :return: type str.
    """
    result = []
    for key in node:
        if isinstance(node[key], dict):
            result.append(f"\n{' ' * indent}{key}: {{")
            result.append(nested_format(node[key], indent + INDENT_STEP))
        else:
            result.append(f"\n{' ' * indent}{key}: "
                          f"{format_specific_value(node[key])}")
    result.append('\n' + ' ' * (indent - INDENT_STEP) + '}')
    return ''.join(result).rstrip()


def format_specific_value(value):
    """
    :param value: type(value) == str
    :return: type str
    """
    return f'{str(value)}' if isinstance(value, str) else vh.format_value(value)
