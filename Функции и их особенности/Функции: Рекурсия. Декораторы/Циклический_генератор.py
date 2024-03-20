def make_linear(x: list):
    values = []

    for i in x:
        if isinstance(i, list):
            values.extend(make_linear(i))
        else:
            values.append(i)
    return values
