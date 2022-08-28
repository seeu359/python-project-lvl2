"""
Default formatter.
This formatter display difference between 2 files as:
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: {
            key: value
        }
}
"""
from gendiff.formatters.formatter_data import stylish_data as st_data


def stylish(introduction):
    return st_data.format_root(introduction, ['{\n'], st_data.INDENT_STEP)
