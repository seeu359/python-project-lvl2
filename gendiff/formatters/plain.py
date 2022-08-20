"""
This formatter display difference between 2 files as:
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to [complex value]
"""
ADDED = 'was added with value:'
REMOVED = 'was removed'
UPDATED = 'was updated. From'
COMPLEX = '[complex value]'
OLD_KEY_VALUES = 'REP-'
UPDATED_KEY_VALUES = 'REP+'


def format_reduction(value):
    """
    Returns the value typed for the given formatter
    :param value: values of any type
    :return: If type(value) is bool: returns str(value).lower
    if  type(value) == int: returns str(value)
    if  type(value) is None: returns null
    Any time return 'str(value)'
    """
    if isinstance(value, bool):
        return f'{str(value).lower()}'
    elif isinstance(value, int):
        return str(value)
    elif value is None:
        return 'null'
    else:
        return f"'{str(value)}'"


def plain(represent):
    """
    A recursive function that distributes keys among formatter functions, or,
    if the key value type is a dictionary, takes the recursive case and passes
    the stored path into itself
    :param represent: type(represent) == dict
    :return: type str.
    """
    def alocate_keys(data, result, path):
        for key in data:
            if isinstance(data.get(key)[0], dict) and data.get(key)[1] == '=':
                alocate_keys(data.get(key)[0], result, path + f'{key}.')
            elif isinstance(data.get(key)[0], dict) and data.get(key)[1] != '=':
                result.append(format_parent(data, key, path))
            if not isinstance(data.get(key)[0], dict):
                result.append(format_child(data, key, path))
        return ''.join(result).strip()
    return alocate_keys(represent, [], '')


def format_parent(data, key, path):
    """
    Takes control if the parent node has children with changed values.
    Returns a formatted value
    :param data: type(data) == dict. Node, where will do format
    :param key: type(key) == str. Key, will be formatted
    :param path: type(path) == str. Path from parent's node to our key
    :return: type == str
    """
    if key.startswith(OLD_KEY_VALUES):
        return f"Property '{path}{key[4:]}' {UPDATED} {COMPLEX} to "
    elif data.get(key)[1] == '-':
        return f"Property '{path}{key}' {REMOVED}\n"
    elif key.startswith(UPDATED_KEY_VALUES):
        return f"{COMPLEX}\n"
    elif data.get(key)[1] == '+':
        return f"Property '{path}{key}' {ADDED} {COMPLEX}\n"


def format_child(data, key, path):
    """
    Takes control if the previous value is not a parent node. Returns a string
    representation of the changed key with the path from the parent node.
    :param data: type(data) == dict. Node, where doing format
    :param key: type(key) == str. Key, will be formatted
    :param path: type(path) == str. Path from parent's node to our key
    :return: type == str
    """
    if key.startswith('REP-'):
        return f"Property '{path}{key[4:]}' {UPDATED}" \
               f" {format_reduction(data.get(key)[0])} to "
    elif key.startswith('REP+'):
        return f"{format_reduction(data.get(key)[0])}\n"
    elif data.get(key)[1] == '+':
        return f"Property '{path}{key}' {ADDED}" \
               f" {format_reduction(data.get(key)[0])}\n"
    elif data.get(key)[1] == '-':
        return f"Property '{path}{key}' {REMOVED}\n"
    else:
        return ''
