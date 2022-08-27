import json
import yaml


STATE_NO_CHANGE = 'no change'
STATE_CHANGE = 'changed'
STATE_REMOTE = 'removed'
STATE_ADDED = 'added'
MARK = {'removed': ('- ', 2),
        'added': ('+ ', 2),
        'no change': ('', 0),
        }


def format_reduction(value, formatter):
    """
    Returns the value typed for the given formatter
    :param value: values of any type
    :param formatter: marks from input datas
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
        if formatter == 'stylish':
            return f"{str(value)}"
        else:
            if isinstance(value, dict):
                return '[complex value]'
            return f"'{str(value)}'"


def get_file_data(path):
    with open(path) as file:
        file_extension = path.split('.')
        if file_extension[-1] == 'json':
            return json.load(file)
        if file_extension[-1] == 'yaml' or file_extension[-1] == 'yml':
            return yaml.safe_load(file)


def get_sorted_keys(*parents):
    result = []
    index = 0
    array = [*parents]
    while index < len(array):
        for key in array[index]:
            if key not in result:
                result.append(key)
        index += 1
    result.sort()
    return result


def get_find_node(node1, node2, child):
    if child in node1:
        return node1, STATE_REMOTE
    else:
        return node2, STATE_ADDED
