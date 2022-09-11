import pytest
from gendiff.generate_diff import generate_diff


@pytest.fixture()
def get_result_json_formatter():
    return generate_diff('tests/fixtures/test_file_nested3.json',
                         'tests/fixtures/test_file_nested4.json',
                         'json')
