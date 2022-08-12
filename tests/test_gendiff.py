from gendiff.generate_diff import generate_diff
import json


RESULT_SIMPLE_STYLISH = open('tests/fixtures/result_stylish_simple').read()
RESULT_SIMPLE_PLAIN = open('tests/fixtures/result_plain_simple').read()
RESULT_NESTED_STYLISH = open('tests/fixtures/result_stylish_nested').read()
RESULT_NESTED_STYLISH2 = open('tests/fixtures/result_stylish_nested2').read()
RESULT_NESTED_PLAIN = open('tests/fixtures/result_plain_nested').read()
RESULT_NESTED_PLAIN2 = open('tests/fixtures/result_plain_nested2').read()


gendiff_simple1 = generate_diff('tests/fixtures/test_file_simple1.json',
                                'tests/fixtures/test_file_simple2.json')

gendiff_simple2 = generate_diff('tests/fixtures/test_file_simple1.json',
                                'tests/fixtures/test_file_simple2.json',
                                'plain')

gendiff_nested1 = generate_diff('tests/fixtures/test_file_nested1.yaml',
                                'tests/fixtures/test_file_nested2.json')

gendiff_nested2 = generate_diff('tests/fixtures/test_file_nested1.json',
                                'tests/fixtures/test_file_nested2.json',
                                'plain')

gendiff_nested3 = generate_diff('tests/fixtures/test_file_nested3.json',
                                'tests/fixtures/test_file_nested4.json')

gendiff_nested4 = generate_diff('tests/fixtures/test_file_nested3.json',
                                'tests/fixtures/test_file_nested4.json',
                                'plain')

gendiff_nested5 = generate_diff('tests/fixtures/test_file_nested3.json',
                                'tests/fixtures/test_file_nested4.json',
                                'json')


def test_generate_diff_simple():
    result_stylish_simple = gendiff_simple1
    result_plain_simple = gendiff_simple2
    assert result_stylish_simple == RESULT_SIMPLE_STYLISH
    assert result_plain_simple == RESULT_SIMPLE_PLAIN


def test_generate_diff_complex():
    result_stylish_nested = gendiff_nested1
    result_plain_nested = gendiff_nested2
    result_stylish_nested2 = gendiff_nested3
    result_plain_nested2 = gendiff_nested4
    result_json = json.loads(gendiff_nested5)
    assert result_stylish_nested == RESULT_NESTED_STYLISH
    assert result_plain_nested == RESULT_NESTED_PLAIN
    assert result_stylish_nested2 == RESULT_NESTED_STYLISH2
    assert result_plain_nested2 == RESULT_NESTED_PLAIN2
    assert isinstance(result_json, dict) is True
    assert result_json['=common']['=setting1'] == 'Value 1'
    assert isinstance(result_json['=group1']['-nest'], dict) is True
