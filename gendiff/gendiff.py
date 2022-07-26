import json


def normalize_type(val):
    if type(val) is bool:
        value = str(val)
        return value.lower()
    elif val is None:
        return 'null'
    else:
        return val


def sorting_keys(*array: list):
    array_lists = [*array]
    result = []
    count_list = len(array_lists)
    index = 0
    while index < count_list:
        for i in array_lists[index]:
            if i not in result:
                result.append(i)
        index += 1
    result.sort()
    return result


def open_file(path):
    with open(path) as file:
        return json.load(file)


def generate_diff(path1, path2):
    file1 = open_file(path1)
    file2 = open_file(path2)
    key_list = sorting_keys(file1, file2)
    result = ''
    for i in key_list:
        first_key = file1.get(i)
        second_key = file2.get(i)
        if first_key == second_key:
            result += f'    {i}: {normalize_type(first_key)}\n'
        elif (first_key is not None) and (second_key is not None):
            result += f'  - {i}: {normalize_type(file1[i])}\n' \
                      f'  + {i}: {normalize_type(file2[i])}\n'
        elif (first_key is not None) and (second_key is None):
            result += f'  - {i}: {normalize_type(first_key)}\n'
        elif (first_key is None) and (second_key is not None):
            result += f'  + {i}: {normalize_type(second_key)}\n'
    return '{\n' + result + '}'
