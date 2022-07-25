from gendiff.gendiff import generate_diff


def test_gendiff():
    result = generate_diff('fixtures/test_file1.json', 'fixtures/test_file2.json')
    assert result == open('fixtures/result_true.txt').read()
