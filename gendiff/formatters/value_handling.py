def format_reduction(value, formatter):
    """
    Returns the value typed for the given formatter
    :param value: values of any type
    :param formatter: type(formatter) == str. Marks from formatter.
    :return: If type(value) is bool: returns str(value).lower
    if  type(value) == int: returns str(value)
    if  type(value) is None: returns null
    Any time return 'str(value)'
    """
    if isinstance(value, bool):
        value = f'{str(value).lower()}'
    elif isinstance(value, int):
        value = str(value)
    elif value is None:
        value = 'null'
    else:
        if formatter == 'stylish':
            value = f"{str(value)}"
        else:
            if isinstance(value, dict):
                return '[complex value]'
            return f"'{str(value)}'"
    return value
