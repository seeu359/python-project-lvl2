from gendiff.generate_diff import generate_diff


def normalize_type(value):
    if type(value) is bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def stylish(notion, replacer=' ', replacer_count=4):

    def get_format(data, result, indent):
        for key in data:
            if isinstance(data.get(key)[0], dict):
                if data.get(key)[1] == '=' or data.get(key)[1] == 'NoAction':
                    result.append(f'{replacer*replacer_count*data.get(key)[2]}'
                                  f'{key}: {{\n')
                elif key.startswith('REP-') or key.startswith('REP+'):
                    result.append(f'{replacer*(replacer_count*data.get(key)[2]-2)}'
                                  f'{data.get(key)[1]} {key[4:]}: {{\n')
                else:
                    result.append(f'{replacer * (replacer_count *  data.get(key)[2] - 2)}'
                                  f'{data.get(key)[1]} {key}: {{\n')

                get_format(data.get(key)[0], result, indent + 1)
            if not isinstance(data.get(key)[0], dict):
                if key.startswith('REP+') or key.startswith('REP-'):
                    if len(normalize_type(data.get(key)[0])) == 0:
                        result.append(f'{replacer * (replacer_count * data.get(key)[2] - 2)}'
                                      f'{data.get(key)[1]} {key[4:]}:'
                                      f'{normalize_type(data.get(key)[0])}\n')
                    else:
                        result.append(f'{replacer * (replacer_count * data.get(key)[2] - 2)}'
                                      f'{data.get(key)[1]} {key[4:]}: '
                                      f'{normalize_type(data.get(key)[0])}\n')
                elif (data.get(key)[1] == '=') or (data.get(key)[1] == 'NoAction'):
                    result.append(f'{replacer * replacer_count * data.get(key)[2]}'
                                  f'{key}: {normalize_type(data.get(key)[0])}\n')
                elif data.get(key)[1] != '=':
                    result.append(f'{replacer * (replacer_count * data.get(key)[2] - 2)}'
                                  f'{   data.get(key)[1]} '
                                  f'{key}: {normalize_type(data.get(key)[0]).strip()}\n')
        result.append(replacer * replacer_count * indent + '}\n')
        return ''.join(result).strip()
    return get_format(notion, ['{\n'], 0)

a = generate_diff('/Users/a1234/python-project-lvl2/tests/fixtures/test_file_nested1.json',
                  '/Users/a1234/python-project-lvl2/tests/fixtures/test_file_nested2.json')

print(stylish(a))