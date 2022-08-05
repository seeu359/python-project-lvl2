ADDED = 'was added with value:'
REMOVED = 'was removed'
UPDATED = 'was updated. From'


def normalize_type(value):
    if type(value) is bool:
        return f"{str(value).lower()}"
    elif value is None:
        return f"null"
    else:
        return f"'{str(value)}'"


def plain(notion):

    def get_format(data, result, path):
        for key in data:
            if isinstance(data.get(key)[0], dict):
                if data.get(key)[1] == '=':
                    get_format(data.get(key)[0], result, path + f'{key}.')
                elif data.get(key)[1] == '-':
                    if key.startswith('REP-'):
                        result.append(f"Property '{path}{key[4:]}' "
                                      f"{UPDATED} [complex value] to ")
                    else:
                        result.append(f"Property '{path}{key}' {REMOVED}\n")
                elif key.startswith('REP+'):
                    result.append('[complex value]\n')
                elif data.get(key)[1] == '+':
                    result.append(f"Property '{path}{key}' "
                                  f"{ADDED} [complex value]\n")
            if not isinstance(data.get(key)[0], dict):
                if key.startswith('REP-'):
                    result.append(f"Property '{path}{key[4:]}' {UPDATED} "
                                  f"{normalize_type(data.get(key)[0])} to ")
                elif key.startswith('REP+'):
                    result.append(f"{normalize_type(data.get(key)[0])}\n")
                elif data.get(key)[1] == '+':
                    result.append(f"Property '{path}{key}' {ADDED} "
                                  f"{normalize_type(data.get(key)[0])}\n")
                elif data.get(key)[1] == '-':
                    result.append(f"Property '{path}{key}' {REMOVED}\n")

        return ''.join(result).strip()
    return get_format(notion, [], '')
