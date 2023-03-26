def select_max_value(x):
    value1 = 0
    value2 = 0

    for i in x:
        if i >= 0:
            value = i
    for i in x:
        if i < value1 and i >= value2:
            value2 = i

    return value1, value2
[5, 10, 10]