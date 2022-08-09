from gendiff.generate_diff import generate_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


RESULT_SIMPLE_STYLISH = open('tests/fixtures/result_stylish_simple.txt').read()
RESULT_SIMPLE_PLAIN = open('tests/fixtures/result_plain_simple').read()
RESULT_STYLISH_FORMAT = open('tests/fixtures/result_stylish_nested.txt').read()
RESULT_PLAIN_FORMAT = open('tests/fixtures/result_plain_nested.txt').read()

gendiff_formatting_simple1 = \
    generate_diff('tests/fixtures/test_file_simple1.json',
                  'tests/fixtures/test_file_simple2.json', stylish)

gendiff_formatting_simple2 = \
    generate_diff('tests/fixtures/test_file_simple1.yml',
                  'tests/fixtures/test_file_simple2.yaml', plain)

gendiff_formatting_nested1 = \
    generate_diff('tests/fixtures/test_file_nested1.yaml',
                  'tests/fixtures/test_file_nested2.json', stylish)

gendiff_formatting2_nested2 = \
    generate_diff('tests/fixtures/test_file_nested1.json',
                  'tests/fixtures/test_file_nested2.yaml', plain)


def test_generate_diff_simple():
    result_stylish_simple = gendiff_formatting_simple1
    result_plain_simple = gendiff_formatting_simple2
    assert result_stylish_simple == RESULT_SIMPLE_STYLISH
    assert result_plain_simple == RESULT_SIMPLE_PLAIN


def test_generate_diff_complex():
    result_stylish_nested = gendiff_formatting_nested1
    result_plain_nested = gendiff_formatting2_nested2
    assert result_stylish_nested == RESULT_STYLISH_FORMAT
    assert result_plain_nested == RESULT_PLAIN_FORMAT
