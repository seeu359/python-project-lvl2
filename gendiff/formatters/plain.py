"""
This formatter display difference between 2 files as:
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to [complex value]
"""

from gendiff.formatters.formatter_data import plain_data


def plain(introduction):
    return plain_data.format_root(introduction, [], '')
