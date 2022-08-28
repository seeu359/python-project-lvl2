from gendiff.formatters.formatter_data import data_handling as dh

INDENT_STEP = 4


def format_root(introduction, result, indent):
    """
    The function, depending on the type of node, passes control to the handler
    functions
    :param introduction: type(introduction) == dict. Takes an internal
    representation from the
    diff
    :param result: type(result) == list. Intermediate result.
    :param indent: type(indent) == dict. Default indent == 4
    :return: type(str)
    """
    for data in introduction:
        if data['type'] == 'parent' and data['state'] != dh.STATE_NO_CHANGE:
            result.append(format_parent(data, indent))
        if data['type'] == 'parent' and data['state'] == dh.STATE_NO_CHANGE:
            result.append(format_parent(data, indent))
            format_root(data.get('children'), result, indent + INDENT_STEP)
        elif data['type'] == 'children':
            result.append(format_child(data, indent))
    result.append(' ' * (indent - 4) + '}\n')
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
    if node['state'] == dh.STATE_NO_CHANGE:
        return f"{' ' * indent}{node['key']}: {{\n"
    else:
        margin = f"{' ' * (indent - dh.MARK[node['state']][1])}"
        return f"{margin}{dh.MARK[node['state']][0]}{node['key']}: {{" \
               f"{alocate_value(node['children'], indent)}\n"


def alocate_value(node, indent):
    if isinstance(node, dict):
        return nested_format(node, indent + INDENT_STEP)
    else:
        return dh.format_reduction(node, 'stylish')


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
    if node['state'] == dh.STATE_CHANGE:
        bracket = '{' if isinstance(node['old_value'], dict) else ''
        result += f"{' ' * (indent - 2)}- {node['key']}: {bracket}" \
                  f"{alocate_value(node['old_value'], indent)}\n"
        bracket = '{' if isinstance(node['new_value'], dict) else ''
        result += f"{' ' * (indent - 2)}+ {node['key']}: {bracket}" \
                  f"{(alocate_value(node['new_value'], indent))}\n"
    else:
        margin = ' ' * (indent - dh.MARK[node['state']][1])
        mark = dh.MARK[node['state']][0]
        result += f"{margin}{mark}{node['key']}: " \
                  f"{(dh.format_reduction(node['value'], 'stylish'))}\n"
    return result


def nested_format(node, indents):
    """
    Function that comprehensively handles a remote or added parent node with
    all children
    :param node: type(node) == dict.
    :param indents: type(indents) == int.
    :return: type str.
    """
    def node_processing(data, indent, result):
        for key in data:
            if isinstance(data[key], dict):
                result.append(f"\n{' ' * indent}{key}: {{")
                node_processing(data[key], indent + INDENT_STEP, result)
            else:
                result.append(f"\n{' ' * indent}{key}: "
                              f"{dh.format_reduction(data[key], 'stylish')}")
        result.append('\n' + ' ' * (indent - INDENT_STEP) + '}')
        return ''.join(result).rstrip()

    return node_processing(node, indents, [])
