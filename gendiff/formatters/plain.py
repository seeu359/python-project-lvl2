ADDED = 'was added with value:'
REMOVED = 'was removed'
UPDATED = 'was updated. From'


def normalize_type(value):
    if type(value) is bool:
        return f"{str(value).lower()}"
    elif value is None:
        return 'null'
    else:
        return f"'{str(value)}'"


def plain(notion):

    def get_format(data, result, path):
        for key in data:
            if isinstance(data.get(key)[0], dict):
                if data.get(key)[1] == '=':
                    get_format(data.get(key)[0], result, path + f'{key}.')
                else:
                    result.append(formatting_dict(data, key, path))
            if not isinstance(data.get(key)[0], dict):
                result.append(formatting_not_dict(data, key, path))
        return ''.join(result).strip()

    return get_format(notion, [], '')


def formatting_dict(data, key, path):
    if data.get(key)[1] == '-':
        if key.startswith('REP-'):
            return (f"Property '{path}{key[4:]}' "
                    f"{UPDATED} [complex value] to ")
        else:
            return f"Property '{path}{key}' {REMOVED}\n"
    elif key.startswith('REP+'):
        return '[complex value]\n'
    elif data.get(key)[1] == '+':
        return f"Property '{path}{key}' {ADDED} [complex value]\n"


def formatting_not_dict(data, key, path):
    if key.startswith('REP-'):
        return f"Property '{path}{key[4:]}' {UPDATED}" \
               f" {normalize_type(data.get(key)[0])} to "
    elif key.startswith('REP+'):
        return f"{normalize_type(data.get(key)[0])}\n"
    elif data.get(key)[1] == '+':
        return f"Property '{path}{key}' {ADDED}" \
               f" {normalize_type(data.get(key)[0])}\n"
    elif data.get(key)[1] == '-':
        return f"Property '{path}{key}' {REMOVED}\n"
    else:
        return ''
