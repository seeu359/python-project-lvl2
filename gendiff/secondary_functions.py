import json
import yaml

def have_key(parent1, parent2, key):
    if parent1.get(key) is not None:
        return [parent1, '-']
    else:
        return [parent2, '+']


def is_not_dictionary(value1, value2):
    if not isinstance(value1, dict) and not isinstance(value2, dict):
        return True
    return False


def open_files(path):
    with open(path) as file:
        if path.endswith('json'):
            return json.load(file)
        if path.endswith('yaml') or path.endswith('yml'):
            return yaml.safe_load(file)


def sorting_keys(*parents):
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