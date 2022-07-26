from gendiff.gendiff import generate_diff


def test_generate_diff():
    result = generate_diff('/Users/a1234/python-project-lvl2/tests/fixtures/test_file1.json',
                           '/Users/a1234/python-project-lvl2/tests/fixtures/test_file2.json')
    assert result == open('/Users/a1234/python-project-lvl2/tests/fixtures/result_true.txt').read()
