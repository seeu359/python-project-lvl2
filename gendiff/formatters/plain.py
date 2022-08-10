ADDED = 'was added with value:'
REMOVED = 'was removed'
UPDATED = 'was updated. From'
COMPLEX = '[complex value]'
OLD_KEY_VALUES = 'REP-'
UPDATED_KEY_VALUES = 'REP+'
RESULT = []


def format_reduction(value):
    if isinstance(value, bool):
        return f"{str(value).lower()}"
    elif isinstance(value, int):
        return str(value)
    elif value is None:
        return 'null'
    else:
        return f"'{str(value)}'"


def plain(notion):

    def distributing_values(data, result, path):
        for key in data:
            if isinstance(data.get(key)[0], dict) and data.get(key)[1] == '=':
                distributing_values(data.get(key)[0], result, path + f'{key}.')
            elif isinstance(data.get(key)[0], dict) and data.get(key)[1] != '=':
                result.append(formatting_dict(data, key, path))
            if not isinstance(data.get(key)[0], dict):
                result.append(formatting_not_dict(data, key, path))
        return ''.join(result).strip()

    return distributing_values(notion, RESULT, '')


def formatting_dict(data, key, path):
    if data.get(key)[1] == '-' and key.startswith(OLD_KEY_VALUES):
        return f"Property '{path}{key[4:]}' {UPDATED} {COMPLEX} to "
    elif data.get(key)[1] == '-':
        return f"Property '{path}{key}' {REMOVED}\n"
    elif key.startswith(UPDATED_KEY_VALUES):
        return f"{COMPLEX}\n"
    elif data.get(key)[1] == '+':
        return f"Property '{path}{key}' {ADDED} {COMPLEX}\n"


def formatting_not_dict(data, key, path):
    if key.startswith('REP-'):
        return f"Property '{path}{key[4:]}' {UPDATED}" \
               f" {format_reduction(data.get(key)[0])} to "
    elif key.startswith('REP+'):
        return f"{format_reduction(data.get(key)[0])}\n"
    elif data.get(key)[1] == '+':
        return f"Property '{path}{key}' {ADDED}" \
               f" {format_reduction(data.get(key)[0])}\n"
    elif data.get(key)[1] == '-':
        return f"Property '{path}{key}' {REMOVED}\n"
    else:
        return ''
