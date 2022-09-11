import pytest

from gendiff.generate_diff import generate_diff
import json


def get_fixture_data(path):
    with open(path) as f:
        file = f.read()
    return file


@pytest.mark.parametrize('path1, path2, expected',
                         [('tests/fixtures/test_file_simple1.json',
                           'tests/fixtures/test_file_simple2.json',
                           get_fixture_data(
                               'tests/fixtures/result_stylish_simple')),
                          ('tests/fixtures/test_file_nested1.yaml',
                           'tests/fixtures/test_file_nested2.json',
                           get_fixture_data(
                               'tests/fixtures/result_stylish_nested')),
                          ('tests/fixtures/test_file_nested3.json',
                           'tests/fixtures/test_file_nested4.json',
                           get_fixture_data(
                               'tests/fixtures/result_stylish_nested2'))]
                         )
def test_generate_diff_stylish(path1, path2, expected):
    assert generate_diff(path1, path2) == expected


@pytest.mark.parametrize('path1, path2, expected', [
                             ('tests/fixtures/test_file_simple1.json',
                              'tests/fixtures/test_file_simple2.json',
                              get_fixture_data(
                                  'tests/fixtures/result_plain_simple')),
                             ('tests/fixtures/test_file_nested1.json',
                              'tests/fixtures/test_file_nested2.json',
                              get_fixture_data(
                                  'tests/fixtures/result_plain_nested')),
                             ('tests/fixtures/test_file_nested3.json',
                              'tests/fixtures/test_file_nested4.json',
                              get_fixture_data(
                                  'tests/fixtures/result_plain_nested2'))]
                         )
def test_generate_diff_plain(path1, path2, expected):
    assert generate_diff(path1, path2, 'plain') == expected


def test_generate_diff_json(get_result_json_formatter):
    assert isinstance(get_result_json_formatter, str) is True
    assert isinstance(json.loads(get_result_json_formatter), list) is True
