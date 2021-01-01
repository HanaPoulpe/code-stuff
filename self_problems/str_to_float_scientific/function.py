def str_to_float_scientific(text: str, default, base: float = 10):
    if text == '':
        return default

    try:
        return float(text)
    except ValueError:
        pass

    for sep in 'Ee\\':
        try:
            (value, exponent) = text.split(sep, maxsplit=2)
        except ValueError:
            continue
        break
    else:
        return default

    try:
        return float(value) * base ** float(exponent)
    except ValueError:
        return default
