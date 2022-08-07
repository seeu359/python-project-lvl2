from gendiff import secondary_functions


def generate_diff(path1, path2, format_name):
    file1 = secondary_functions.open_files(path1)
    file2 = secondary_functions.open_files(path2)
    result = dict()
    keys_list = secondary_functions.sorting_keys(file1, file2)
    indent = 1
    for key in keys_list:
        if isinstance(file1.get(key), dict) and \
                isinstance(file2.get(key), dict):
            result[key] = [formatting_search(file1.get(key),
                                             file2.get(key)),
                           '=', indent]
        elif isinstance(file1.get(key), dict) and key not in file2:
            result[key] = [not_formatting_search(file1.get(key),
                                                 indent + 1),
                           '-', indent]
        elif key not in file1 and isinstance(file2.get(key), dict):
            result[key] = [not_formatting_search(file2.get(key),
                                                 indent + 1),
                           '+', indent]
        else:
            value = formatting_search(file1, file2, indent)
            result.update(value)
    return format_name(result)


def formatting_search(parent1, parent2, indent=2):
    result = dict()
    keys_list = secondary_functions.sorting_keys(parent1, parent2)
    for key in keys_list:
        if key in parent1 and key in parent2:
            if secondary_functions.is_not_dictionary(parent1.get(key),
                                                     parent2.get(key)):
                value = simple_formatting(parent1, parent2, key, indent)
                result.update(value)
            elif isinstance(parent1.get(key), dict) \
                    and isinstance(parent2.get(key), dict):
                result[key] = [formatting_search(parent1.get(key),
                                                 parent2.get(key),
                                                 indent + 1), '=', indent]
            else:
                value = complex_formatting(parent1, parent2, key, indent)
                result.update(value)
        else:
            result[key] = formatting_search3(secondary_functions.have_key
                                             (parent1, parent2, key),
                                             indent, key)
    return result


def simple_formatting(parent1, parent2, key, indent):
    result = dict()
    if parent1[key] == parent2[key]:
        result[key] = [parent1.get(key), '=', indent]
        return result
    elif parent1[key] != parent2[key]:
        result[f'REP-{key}'] = [parent1.get(key), '-', indent]
        result[f'REP+{key}'] = [parent2.get(key), '+', indent]
        return result


def complex_formatting(parent1, parent2, key, indent):
    result = dict()
    if isinstance(parent1.get(key), dict) and\
            not isinstance(parent2.get(key), dict):
        result[f'REP-{key}'] = [not_formatting_search(parent1.get(key),
                                                      indent + 1),
                                '-', indent]
        result[f'REP+{key}'] = [parent2.get(key), '+', indent]
        return result
    elif not isinstance(parent1.get(key), dict) and\
            isinstance(parent2.get(key), dict):
        result = [indent, '-', parent1.get(key),
                  not_formatting_search(parent2.get(key), indent + 1)]
        return result


def not_formatting_search(parent, indent):
    result = dict()
    keys_list = secondary_functions.sorting_keys(parent)
    for key in keys_list:
        if not isinstance(parent.get(key), dict):
            result[key] = ([parent.get(key), 'NoAction', indent])
        elif isinstance(parent.get(key), dict):
            result[key] = [not_formatting_search(parent.get(key),
                                                 indent + 1),
                           'NoAction', indent]
    return result


def formatting_search3(parent, indent, key):
    if not isinstance(parent[0].get(key), dict):
        return [parent[0].get(key), parent[1], indent]
    if isinstance(parent[0].get(key), dict):
        result = [not_formatting_search(parent[0].get(key),
                                        indent + 1),
                  parent[1], indent]
        return result
