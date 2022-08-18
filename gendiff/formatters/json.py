"""
This formatter display difference between 2 files as:
{"+a": 1, "b": {"=c": null, "-d": "foo"}}.
The output of a command json_loads(output) can be represented as a type(dict).
"""

OLD_KEY_VALUE = 'REP-'
UPDATED_KEY_VALUE = 'REP+'
NOT_FORMAT = 'NoAction'


def format_reduction(value):
    """
    Returns the value typed for the given formatter
    :param value: values of any type
    :return: If value type == bool: returns str(value).lower
    if value type == int: returns str(value)
    if value type == None: returns null
    Any time return "str(value)"
        """
    if type(value) is bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return str(value)
    else:
        return f'"{value}"'


def json(represent):
    """
    Recursive function, takes the difference with the internal representation
    of each key and distributes each key to the formatter depending on its
    value. The output of a command json_loads(output) can be represented as a
    type(dict).
    :param represent: type(represent) == dict
    :return: type str
    """
    def distributing_keys(node, result):
        for key in node:
            if isinstance(node.get(key)[0], dict):
                result.append(formatting_parent(node, key))
                distributing_keys(node.get(key)[0], result)
            elif not isinstance(node.get(key)[0], dict):
                result.append(formatting_child(node, key))
        result[-1] = result[-1][:-2]
        result.append('}, ')
        return ''.join(result).strip()[:-1]
    return distributing_keys(represent, ['{'])


def formatting_parent(node, key):
    """
    Takes control from the parent. Depending on the different values in 2 files,
    takes the final value. Different displays in first symbol keys.
    If keys[0] == '+': Key was added in second files
    If keys[0] == '-': Key was removed in second files
    If keys[0] == '=': Key in both files.
    :param node: type(node) == dict. Node, where will do format
    :param key: type(key) == str. Key, will be formatted
    :return: type str.
    """
    options = {'-': f'"-{key}": {{',
               '+': f'"+{key}": {{',
               '=': f'"={key}": {{'
               }
    if key.startswith(OLD_KEY_VALUE):
        return f'"-{key[4:]}": {{'
    elif key.startswith(UPDATED_KEY_VALUE):
        return f'"+{key[4:]}": {{'
    elif node.get(key)[1] == NOT_FORMAT:
        return f'"{key}": {{'
    else:
        return options[node.get(key)[1]]


def formatting_child(node, key):
    """
    Takes control if the previous key is not the parent node. Adds to the final
    result a key with one of the first characters ('-', '+', '+') and the
    formatted value for this key.
    :param node: type(node) == dict. Node, where will do format
    :param key: type(key) == str. Key, will be formatted
    :return: type str
    """
    options = {'-': f'"-{key}": {format_reduction(node.get(key)[0])}, ',
               '+': f'"+{key}": {format_reduction(node.get(key)[0])}, ',
               '=': f'"={key}": {format_reduction(node.get(key)[0])}, '
               }
    if key.startswith(OLD_KEY_VALUE):
        return f'"-{key[4:]}": {format_reduction(node.get(key)[0])}, '
    elif key.startswith(UPDATED_KEY_VALUE):
        return f'"+{key[4:]}": {format_reduction(node.get(key)[0])}, '
    elif node.get(key)[1] == NOT_FORMAT:
        return f'"{key}": {format_reduction(node.get(key)[0])}, '
    else:
        return options[node.get(key)[1]]
