from gendiff.generate_diff import generate_diff
from gendiff.formatter import stylish

RESULT_SIMPLE_FORMAT = open('tests/fixtures/result_simple_true.txt').read()
RESULT_NESTED_FORMAT = open('tests/fixtures/result_nested_true.txt').read()


def test_generate_diff_simple():
    result_json_simple = generate_diff('tests/fixtures/test_file_simple1.json',
                                       'tests/fixtures/test_file_simple2.json')
    result_yaml_simple = generate_diff('tests/fixtures/test_file_simple1.yml',
                                       'tests/fixtures/test_file_simple2.yaml')
    assert isinstance(result_json_simple['follow'], list) is True
    assert isinstance(result_yaml_simple['follow'], list) is True
    assert result_json_simple['proxy'][2] == 1
    assert result_yaml_simple['verbose'][2] == True
    assert stylish(result_json_simple) == RESULT_SIMPLE_FORMAT
    assert stylish(result_yaml_simple) == RESULT_SIMPLE_FORMAT


def test_generate_diff_complex():
    result_json_nested = generate_diff('tests/fixtures/test_file_nested1.json',
                                       'tests/fixtures/test_file_nested2.json')
    result_yaml_nested = generate_diff('tests/fixtures/test_file_nested1.yaml',
                                       'tests/fixtures/test_file_nested2.yaml')
    assert stylish(result_json_nested) == RESULT_NESTED_FORMAT
    assert stylish(result_yaml_nested) == RESULT_NESTED_FORMAT
