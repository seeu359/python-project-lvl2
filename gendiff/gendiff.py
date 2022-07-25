import json


def normalize_type(val):
    if type(val) is bool:
        value = str(val)
        return value.lower()
    elif type(val) is None:
        return 'null'
    else:
        return val


def open_file(path):
    with open(path) as file:
        return json.load(file)


def generate_diff(path1, path2):
    file1 = open_file(path1)
    file2 = open_file(path2)
    key_list = []
    result = ''
    for key1 in file1.keys():
        key_list.append(key1)
    for key2 in file2.keys():
        if key2 not in key_list:
            key_list.append(key2)
    key_list.sort()
    for i in key_list:
        if (file1.get(i) is not None) and (file2.get(i) is not None):
            if file1[i] == file2[i]:
                result += f'    {i}: {normalize_type(file1[i])}\n'
            elif file1[i] != file2[i]:
                result += f'  - {i}: {normalize_type(file1[i])}\n' \
                          f'  + {i}: {normalize_type(file2[i])}\n'
        elif (file1.get(i) is not None) and (file2.get(i) is None):
            result += f'  - {i}: {normalize_type(file1[i])}\n'
        elif (file1.get(i) is None) and (file2.get(i) is not None):
            result += f'  + {i}: {normalize_type(file2[i])}\n'
    return '{\n' + result + '}'
