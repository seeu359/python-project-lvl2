"""
The module compares 2 files(json, yaml) and outputs the difference with an
internal representation of each key. Output type - format dictionary:
{key: name of key,
 type: parent/children,
 state: change/no change/removed/added,
 value: key value,
 }
"""
from gendiff import parser
from gendiff import build_diff as bd
from gendiff.formatters.stylish import format_diff as stylish
from gendiff.formatters.json import format_diff as json
from gendiff.formatters.plain import format_diff as plain


formatter_selection = {'stylish': stylish,
                       'json': json,
                       'plain': plain
                       }


def generate_diff(file1, file2, format_name='stylish'):
    """
    :param file1: type(file1) == str. Path to file1
    :param file2: type(file2) == str. Path to file2
    :param format_name: type(format_name) == str. Choice of the formatter.
    Default formatter == stylish.
    :return: type dict
    """
    file1_data = parser.get_file_data(file1)
    file2_data = parser.get_file_data(file2)
    return formatter_selection[format_name](bd.make_diff(file1_data,
                                                         file2_data))
