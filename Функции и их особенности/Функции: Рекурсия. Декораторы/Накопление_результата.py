def result_accumulator(f):
    values = []

    def wraper(*args, method: str = "accumulate", **kwargs):
        nonlocal values

        values.append(f(*args, **kwargs))

        if method == "drop":
            temp = values.copy()
            values = []
            return temp

    return wraper
