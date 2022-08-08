REPLACER = ' '
REPLACER_COUNT = 2
INDENT = REPLACER * REPLACER_COUNT
OLD_KEY_VALUE = 'REP-'
UPDATED_KEY_VALUE = 'REP+'
NOT_FORMAT = 'NoAction'


def normalize_type(value):
    if type(value) is bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def json(data):

    def get_format(notion, result, indent):
        for key in notion:
            if isinstance(notion.get(key)[0], dict):
                result.append(formatting_dict1(notion, key))
                get_format(notion.get(key)[0], result, indent + 1)
            elif not isinstance(notion.get(key)[0], dict):
                result.append(formatting_not_dict(notion, key))
        result.append(f'{INDENT * (indent - 1)}}}\n')
        return ''.join(result).strip()
    return get_format(data, ['{\n'], 1)


def formatting_dict1(data, key):
    options = {'-': f'{INDENT * data.get(key)[2]}"{key}"-: {{\n',
               '+': f'{INDENT * data.get(key)[2]}"{key}"+: {{\n',
               '=': f'{INDENT * data.get(key)[2]}"{key}": {{\n'
               }
    if key.startswith(OLD_KEY_VALUE):
        return f'{INDENT * data.get(key)[2]}"{key[4:]}"-: {{\n'
    elif key.startswith(UPDATED_KEY_VALUE):
        return f'{INDENT * data.get(key)[2]}"{key[4:]}"+: ' \
               f'"{normalize_type(data.get(key)[0])}"\n'
    elif data.get(key)[1] == NOT_FORMAT:
        return f'{INDENT * data.get(key)[2]}"{key}": {{\n'
    else:
        return options[data.get(key)[1]]


def formatting_not_dict(data, key):
    options = {'-': f'{INDENT * data.get(key)[2]}"{key}"-:'
                    f'{normalize_type(data.get(key)[0])} \n',
               '+': f'{INDENT * data.get(key)[2]}"{key}"+:'
                    f'{normalize_type(data.get(key)[0])}\n',
               '=': f'{INDENT * data.get(key)[2]}"{key}": '
                    f'{data.get(key)[0]}\n'
               }
    if key.startswith(OLD_KEY_VALUE):
        return f'{INDENT * data.get(key)[2]}"{key[4:]}"-: ' \
               f'{normalize_type(data.get(key)[0])}\n'
    elif key.startswith(UPDATED_KEY_VALUE):
        return f'{INDENT * data.get(key)[2]}"{key[4:]}"+: ' \
               f'{normalize_type(data.get(key)[0])}\n'
    elif data.get(key)[1] == NOT_FORMAT:
        return f'{INDENT * data.get(key)[2]}"{key}": ' \
               f'"{normalize_type(data.get(key)[0])}"\n'
    else:
        return options[data.get(key)[1]]


def formatting_unchanged_key(data, key):
    return f'{INDENT * data.get(key)[2]}"{key}": {data.get(key)[0]}\n'


def formatting_unchanged_dict(data, key):
    return f'{INDENT * data.get(key)[2]}"{key}": {{\n'
