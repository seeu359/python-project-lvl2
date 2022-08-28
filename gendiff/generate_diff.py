"""
The module compares 2 files and returns a dictionary with an internal
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

from gendiff.formatters.formatter_data import data_handling as dh, \
    node_handling as nh
from gendiff.formatters.stylish import stylish
from gendiff.formatters.json import json_output as json
from gendiff.formatters.plain import plain


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
    file1_data = dh.get_file_data(file1)
    file2_data = dh.get_file_data(file2)
    result = []
    keys_list = dh.get_sorted_keys(file1_data, file2_data)
    for root in keys_list:
        if root in file1_data and root in file2_data:
            if (isinstance(file1_data[root], dict) and isinstance(
                    file2_data[root], dict)):
                result.append({'key': root,
                              'type': 'parent',
                               'state': dh.STATE_NO_CHANGE,
                               'children': nh.format_child(file1_data.get(root),
                                                           file2_data.get(root))
                               })
                continue
            else:
                result.append(nh.compare_values(file1_data, file2_data, root))
                continue
        elif root in file1_data or root in file2_data:
            node = dh.get_find_node(file1_data, file2_data, root)
            if isinstance(node[0].get(root), dict):
                result.append({'key': root,
                              'type': 'parent',
                               'state': node[1],
                               'children': node[0].get(root)
                               })
            else:
                result.append(nh.flat_structure_process(root, node))
    return formatter_selection[format_name](result)
