from gendiff import generate_diff


def test_generate_diff():
    result_json = generate_diff('tests/fixtures/test_file1.json',
                                        'tests/fixtures/test_file2.json')
    result_yaml = generate_diff('tests/fixtures/test_file1.yml',
                                'tests/fixtures/test_file2.yaml')
    assert result_json == open('tests/fixtures/result_json_true.txt').read()
    assert result_yaml == open('tests/fixtures/result_yaml_true.txt').read()
