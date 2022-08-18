"""
The module compares 2 files () and returns a dictionary with an internal
representation of each key. The value of each key is a list of the form:
list[0] = the actual value of the key
list[1] = modification type
    if list[1] == '=': The value of the key has either not changed,
    or the key is a paren that is also present in the second file
    if list[1] == '+': The key has been added in the second file
    if list[1] == '-': Key has been removed in the second file
    If the key is present in both files, but its value in the second file has
    changed, 2 keys are output, the first one starts with 'REP-{key}' and
    represents the value of the first file, the second with 'REP+{key}' and
    represents the updated value.
list[2] = The parent of the current node.
    If the node is the root - the value is an empty string
"""

from gendiff.lib import data_handling, node_handling
from gendiff.formatters.stylish import stylish
from gendiff.formatters.json import json
from gendiff.formatters.plain import plain


NOT_CHANGED = '='
ADDED = '+'
REMOVED = '-'

formatter_selection = {'stylish': stylish,
                       'json': json,
                       'plain': plain}


def generate_diff(file1, file2, format_name='stylish'):
    """
    :param file1: type(file1) == str. Path to file1
    :param file2: type(file2) == str. Path to file2
    :param format_name: type(format_name) == str. Choice of the formatter.
    Default formatter == stylish.
    :return: type dict
    """
    file1 = data_handling.get_file_data(file1)
    file2 = data_handling.get_file_data(file2)
    result = dict()
    keys_list = data_handling.get_sorted_keys(file1, file2)
    parent = ''
    for key in keys_list:
        if isinstance(file1.get(key), dict) and \
                isinstance(file2.get(key), dict):
            result[key] = [node_handling.format_parent
                           (file1.get(key), file2.get(key),
                            parent + key), NOT_CHANGED, parent]
        if isinstance(file1.get(key), dict) and key not in file2:
            result[key] = [node_handling.process_without_format
                           (file1.get(key), f'{parent}{key}'), REMOVED, parent]
        if key not in file1 and isinstance(file2.get(key), dict):
            result[key] = [node_handling.process_without_format
                           (file2.get(key), f'{parent}{key}'), ADDED, parent]
        else:
            value = node_handling.format_parent(file1,
                                                file2, parent)
            result.update(value)
    return formatter_selection[format_name](result)
