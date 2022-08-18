import json
import yaml

ADDED = '+'
REMOVED = '-'


def define_node(node1, node2, key):
    if node1.get(key) is not None:
        return [node1, REMOVED]
    elif node2.get(key) is not None:
        return [node2, ADDED]


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
