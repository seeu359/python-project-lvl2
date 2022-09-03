from gendiff.generate_diff import generate_diff
import json


gen_diff_simple_stylish = generate_diff('tests/fixtures/test_file_simple1.json',
                                        'tests/fixtures/test_file_simple2.json')

gen_diff_nested_stylish = generate_diff('tests/fixtures/test_file_nested1.yaml',
                                        'tests/fixtures/test_file_nested2.json')

gen_diff_nested_stylish2 = generate_diff('tests/fixtures/test_file_nested3.'
                                         'json',
                                         'tests/fixtures/test_file_nested4.'
                                         'json')

gen_diff_simple_plain = generate_diff('tests/fixtures/test_file_simple1.json',
                                      'tests/fixtures/test_file_simple2.json',
                                      'plain')

gen_diff_nested_plain = generate_diff('tests/fixtures/test_file_nested1.json',
                                      'tests/fixtures/test_file_nested2.json',
                                      'plain')

gen_diff_nested_plain2 = generate_diff('tests/fixtures/test_file_nested3.json',
                                       'tests/fixtures/test_file_nested4.json',
                                       'plain')

gen_diff_json = generate_diff('tests/fixtures/test_file_nested3.json',
                              'tests/fixtures/test_file_nested4.json', 'json')


def test_generate_diff_simple(_result_stylish_simple, _result_plain_simple):
    result_stylish_simple = gen_diff_simple_stylish
    result_plain_simple = gen_diff_simple_plain
    assert result_stylish_simple == _result_stylish_simple
    assert result_plain_simple == _result_plain_simple


def test_generate_diff_stylish(_result_stylish_nested1,
                               _result_stylish_nested2):
    result_stylish_nested = gen_diff_nested_stylish
    result_stylish_nested2 = gen_diff_nested_stylish2
    assert result_stylish_nested == _result_stylish_nested1
    assert result_stylish_nested2 == _result_stylish_nested2


def test_generate_diff_plain(_result_plain_nested1, _result_plain_nested2):
    result_plain_nested = gen_diff_nested_plain
    result_plain_nested2 = gen_diff_nested_plain2
    assert result_plain_nested == _result_plain_nested1
    assert result_plain_nested2 == _result_plain_nested2


def test_generate_diff_json():
    assert isinstance(gen_diff_json, str) is True
    assert isinstance(json.loads(gen_diff_json), list) is True
