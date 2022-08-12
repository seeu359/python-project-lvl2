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
REPLACER = ' '
REPLACER_COUNT = 4
OLD_KEY_VALUE = 'REP-'
UPDATED_KEY_VALUE = 'REP+'
NO_ACTION = 'NoAction'


def format_reduction(value):
    """
    Returns the value typed for the given formatter
    :param value: type(value) == values of any type
    :return: if type(value) is bool return str(value).lower()
    if type(value) is None return 'null'
    else return str(value)
    """
    if type(value) is bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def stylish(represent):
    """
    A recursive function that distributes keys among formatter functions, or,
    if the key value type is a dictionary, takes the recursive case and passes
    the stored path into itself
    :param represent: type(represent) == dict
    :return: type str
    """
    def distributing_keys(node, result, indent):
        for key in node:
            if isinstance(node.get(key)[0], dict):
                result.append(formatting_parent(node, key, indent))
                distributing_keys(node.get(key)[0], result, indent + 1)
            if not isinstance(node.get(key)[0], dict):
                result.append(formatting_child(node, key, indent))
        result.append(REPLACER * REPLACER_COUNT * (indent - 1) + '}\n')
        return ''.join(result).strip()
    return distributing_keys(represent, ['{\n'], 1)


def formatting_parent(node, key, indent):
    """
    Takes control from the parent. The difference is displayed as one of the
    characters before the key.The '+' sign indicates that the node was added
    in the second file. Sign '-' that the node was deleted in the second file.
    The absence of a sign in front of the parent means that its internal
    structure has changed
    :param node: type(node) == dict
    :param key: type(key) == str
    :param indent: type(indent) == int
    :return: type str
    """
    if node.get(key)[1] == '=' or node.get(key)[1] == NO_ACTION:
        return (f'{REPLACER * REPLACER_COUNT * indent}'
                f'{key}: {{\n')
    elif key.startswith(OLD_KEY_VALUE) or key.startswith(UPDATED_KEY_VALUE):
        return (f'{REPLACER * (REPLACER_COUNT * indent - 2)}'
                f'{node.get(key)[1]} {key[4:]}: {{\n')
    else:
        return (f'{REPLACER * (REPLACER_COUNT * indent - 2)}'
                f'{node.get(key)[1]} {key}: {{\n')


def formatting_child(node, key, indent):
    """
    Takes control if key value is not a dictionary. Returns a key preceded by a
    key character that indicates changes made to the given key.
    If in front of the key '+': Key was added in second file
    If '-': Key was removed in second file
    If no symbols before the key: key values was not changed
    If the names of two neighboring keys are the same, key values was changed in
    second file.
    :param node: type(node) == dict
    :param key: type(key) == str
    :param indent: type(indent) == int
    :return: type str
    """
    if key.startswith(OLD_KEY_VALUE) or key.startswith(UPDATED_KEY_VALUE):
        return f'{REPLACER * (REPLACER_COUNT * indent - 2)}' \
               f'{node.get(key)[1]} {key[4:]}: ' \
               f'{format_reduction(node.get(key)[0])}\n'
    elif (node.get(key)[1] == '=') or (node.get(key)[1] == NO_ACTION):
        return f'{REPLACER * REPLACER_COUNT * indent}' \
               f'{key}: {format_reduction(node.get(key)[0])}\n'
    elif node.get(key)[1] != '=':
        return f'{REPLACER * (REPLACER_COUNT * indent - 2)}' \
               f'{node.get(key)[1]} {key}: ' \
               f'{format_reduction(node.get(key)[0]).strip()}\n'
