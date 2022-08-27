from gendiff.generate_diff import generate_diff


gen_diff_simple1 = generate_diff('tests/fixtures/test_file_simple1.json',
                                 'tests/fixtures/test_file_simple2.json')

gen_diff_simple2 = generate_diff('tests/fixtures/test_file_simple1.json',
                                 'tests/fixtures/test_file_simple2.json',
                                 'plain')

gen_diff_nested1 = generate_diff('tests/fixtures/test_file_nested1.yaml',
                                 'tests/fixtures/test_file_nested2.json')

gen_diff_nested2 = generate_diff('tests/fixtures/test_file_nested1.json',
                                 'tests/fixtures/test_file_nested2.json',
                                 'plain')

gen_diff_nested3 = generate_diff('tests/fixtures/test_file_nested3.json',
                                 'tests/fixtures/test_file_nested4.json')

gen_diff_nested4 = generate_diff('tests/fixtures/test_file_nested3.json',
                                 'tests/fixtures/test_file_nested4.json',
                                 'plain')

gen_diff_nested5 = generate_diff('tests/fixtures/test_file_nested3.json',
                                 'tests/fixtures/test_file_nested4.json',
                                 'json')


def test_generate_diff_simple():
    with open('tests/fixtures/result_stylish_simple') as rss:
        _result_stylish_simple = rss.read()
    with open('tests/fixtures/result_plain_simple') as rps:
        _result_plain_simple = rps.read()
    result_stylish_simple = gen_diff_simple1
    result_plain_simple = gen_diff_simple2
    assert result_stylish_simple == _result_stylish_simple
    assert result_plain_simple == _result_plain_simple


def test_generate_diff_complex():
    with open('tests/fixtures/result_stylish_nested') as rsn1:
        _result_stylish_nested1 = rsn1.read()
    with open('tests/fixtures/result_stylish_nested2') as rsn2:
        _result_stylish_nested2 = rsn2.read()
    with open('tests/fixtures/result_plain_nested') as rpn1:
        _result_plain_nested1 = rpn1.read()
    with open('tests/fixtures/result_plain_nested2') as rpn2:
        _result_plain_nested2 = rpn2.read()
    result_stylish_nested = gen_diff_nested1
    result_plain_nested = gen_diff_nested2
    result_stylish_nested2 = gen_diff_nested3
    result_plain_nested2 = gen_diff_nested4
    assert result_stylish_nested == _result_stylish_nested1
    assert result_plain_nested == _result_plain_nested1
    assert result_stylish_nested2 == _result_stylish_nested2
    assert result_plain_nested2 == _result_plain_nested2
    assert isinstance(gen_diff_nested5, str) is True
