from gendiff import generate_diff


def test_generate_diff():
    result = generate_diff('tests/fixtures/test_file1.json',
                           'tests/fixtures/test_file2.json')
    assert result == open('tests/fixtures/result_true.txt').read()
