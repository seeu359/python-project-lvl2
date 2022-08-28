"""
The module compares 2 files(json, yaml) and outputs the difference with an
internal representation of each key. Output type - format dictionary:
{key: name of key,
 type: parent/children,
 state: change/no change/removed/added,
 value: key value,
 }
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
