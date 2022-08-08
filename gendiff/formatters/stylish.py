REPLACER = ' '
REPLACER_COUNT = 4
OLD_KEY_VALUE = 'REP-'
UPDATED_KEY_VALUE = 'REP+'


def normalize_type(value):
    if type(value) is bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def stylish(notion):

    def get_format(data, result, indent):
        for key in data:
            if isinstance(data.get(key)[0], dict):
                result.append(formatting_dict(data, key))
                get_format(data.get(key)[0], result, indent + 1)
            if not isinstance(data.get(key)[0], dict):
                result.append(formatting_not_dict(data, key))
        result.append(REPLACER * REPLACER_COUNT * indent + '}\n')
        return ''.join(result).strip()
    return get_format(notion, ['{\n'], 0)


def formatting_dict(parent, key):
    if parent.get(key)[1] == '=' or parent.get(key)[1] == 'NoAction':
        return (f'{REPLACER * REPLACER_COUNT * parent.get(key)[2]}'
                f'{key}: {{\n')
    elif key.startswith(OLD_KEY_VALUE) or key.startswith(UPDATED_KEY_VALUE):
        return (f'{REPLACER * (REPLACER_COUNT * parent.get(key)[2] - 2)}'
                f'{parent.get(key)[1]} {key[4:]}: {{\n')
    else:
        return (f'{REPLACER * (REPLACER_COUNT * parent.get(key)[2] - 2)}'
                f'{parent.get(key)[1]} {key}: {{\n')


def formatting_not_dict(parent, key):
    if key.startswith(OLD_KEY_VALUE) or key.startswith(UPDATED_KEY_VALUE):
        if len(normalize_type(parent.get(key)[0])) == 0:
            return f'{REPLACER * (REPLACER_COUNT * parent.get(key)[2] - 2)}' \
                   f'{parent.get(key)[1]} {key[4:]}:' \
                   f'{normalize_type(parent.get(key)[0])}\n'
        else:
            return f'{REPLACER * (REPLACER_COUNT * parent.get(key)[2] - 2)}' \
                   f'{parent.get(key)[1]} {key[4:]}: ' \
                   f'{normalize_type(parent.get(key)[0])}\n'
    elif (parent.get(key)[1] == '=') or (parent.get(key)[1] == 'NoAction'):
        return f'{REPLACER * REPLACER_COUNT * parent.get(key)[2]}' \
               f'{key}: {normalize_type(parent.get(key)[0])}\n'
    elif parent.get(key)[1] != '=':
        return(f'{REPLACER * (REPLACER_COUNT * parent.get(key)[2] - 2)}'
               f'{parent.get(key)[1]} '
               f'{key}: {normalize_type(parent.get(key)[0]).strip()}\n')
