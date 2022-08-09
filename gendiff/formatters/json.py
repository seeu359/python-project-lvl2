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
    elif isinstance(value, int):
        return str(value)
    else:
        return f'"{value}"'


def json(data):

    def get_format(notion, result, indent):
        for key in notion:
            if isinstance(notion.get(key)[0], dict):
                result.append(formatting_dict(notion, key))
                get_format(notion.get(key)[0], result, indent + 1)
            elif not isinstance(notion.get(key)[0], dict):
                result.append(formatting_not_dict(notion, key))
        result[-1] = result[-1][:-2]
        result.append('}, ')
        return ''.join(result).strip()[:-1]
    return get_format(data, ['{'], 1)


def formatting_dict(data, key):
    options = {'-': f'"-{key}": {{',
               '+': f'"+{key}": {{',
               '=': f'"={key}": {{'
               }
    if key.startswith(OLD_KEY_VALUE):
        return f'"-{key[4:]}": {{'
    elif key.startswith(UPDATED_KEY_VALUE):
        return f'"+{key[4:]}": {{'
    elif data.get(key)[1] == NOT_FORMAT:
        return f'"{key}": {{'
    else:
        return options[data.get(key)[1]]


def formatting_not_dict(data, key):
    options = {'-': f'"-{key}": {normalize_type(data.get(key)[0])}, ',
               '+': f'"+{key}": {normalize_type(data.get(key)[0])}, ',
               '=': f'"={key}": {normalize_type(data.get(key)[0])}, '
               }
    if key.startswith(OLD_KEY_VALUE):
        return f'"-{key[4:]}": {normalize_type(data.get(key)[0])}, '
    elif key.startswith(UPDATED_KEY_VALUE):
        return f'"+{key[4:]}": {normalize_type(data.get(key)[0])}, '
    elif data.get(key)[1] == NOT_FORMAT:
        return f'"{key}": {normalize_type(data.get(key)[0])}, '
    else:
        return options[data.get(key)[1]]
