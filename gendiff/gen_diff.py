import json
import yaml


def single_key_bypass(skirt, debth):

    def bypass(key, indent):
        result = dict()
        for i in key:
            if isinstance(key.get(i), dict):
                result[i] = [bypass(key.get(i), indent + 1),
                             'NoAction', indent + 1]
            elif not isinstance(key.get(i), dict):
                result[i] = [key.get(i), 'NoAction', indent + 1]
        return result
    return bypass(skirt, debth)


def sorting_keys(*array: list):
    array_keys = [*array]
    result = []
    count_list = len(array_keys)
    index = 0
    while index < count_list:
        for i in array_keys[index]:
            if i not in result:
                result.append(i)
        index += 1
    result.sort()
    return result


def open_file(path):
    with open(path) as file:
        if path.endswith('json'):
            return json.load(file)
        if path.endswith('yaml') or path.endswith('yml'):
            return yaml.safe_load(file)


def generate_diff(path1, path2):
    file1 = open_file(path1)
    file2 = open_file(path2)

    def find_diff(parent_value1, parent_value2, indent):
        final_difference = dict()
        sort_keys = sorting_keys(parent_value1, parent_value2)
        for key in sort_keys:
            if key in parent_value1 \
                    and key in parent_value2:
                if isinstance(parent_value1.get(key), dict) and isinstance(parent_value2.get(key), dict):
                    final_difference[key] = \
                        [find_diff(parent_value1.get(key), parent_value2.get(key), indent + 1), '=', indent]
                elif isinstance(parent_value1.get(key), dict) and not isinstance(parent_value2.get(key), dict):
                    final_difference[f'REP-{key}'] = [single_key_bypass(parent_value1.get(key), indent), '-', indent]
                    final_difference[f'REP+{key}'] = [parent_value2.get(key), '+', indent]
                elif not isinstance(parent_value1.get(key), dict) and isinstance(parent_value2.get(key), dict):
                    final_difference[f'REP-{key}'] = [parent_value1.get(key), '-', indent]
                    final_difference[f'REP+{key}'] = [single_key_bypass(parent_value2.get(key), indent), '+', indent]
                elif parent_value1.get(key) is not dict and parent_value2.get(key) is not dict:
                    if parent_value1.get(key) == parent_value2.get(key):
                        final_difference[key] = [parent_value1.get(key), '=', indent]
                    elif parent_value1.get(key) != parent_value2.get(key):
                        final_difference[f'REP-{key}'] = [parent_value1.get(key), '-', indent]
                        final_difference[f'REP+{key}'] = [parent_value2.get(key), '+', indent]
                    elif (isinstance(parent_value1.get(key), dict) and parent_value2[key] is not dict) \
                            or (parent_value1[key] is not dict and isinstance(parent_value2.get(key), dict)):
                        final_difference[key] = [parent_value1.get(key), '-', indent]
                        final_difference[key] = [parent_value2.get(key), '-', indent]
            elif key in parent_value1 and key not in parent_value2:
                if isinstance(parent_value1.get(key), dict):
                    final_difference[key] = [single_key_bypass(parent_value1.get(key), indent), '-', indent]
                elif not isinstance(parent_value1.get(key), dict):
                    final_difference[key] = [parent_value1.get(key), '-', indent]
            elif (key not in parent_value1) and (key in parent_value2):
                if isinstance(parent_value2.get(key), dict):
                    final_difference[key] = [single_key_bypass(parent_value2.get(key), indent), '+', indent]
                elif not isinstance(parent_value2.get(key), dict):
                    final_difference[key] = [parent_value2.get(key), '+', indent]
        return final_difference
    return find_diff(file1, file2, 1)
