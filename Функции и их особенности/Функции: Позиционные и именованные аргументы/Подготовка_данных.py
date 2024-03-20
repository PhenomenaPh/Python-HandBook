def to_string(*args, sep=" ", end="\n"):
    values = list(map(str, args))
    return sep.join(values) + end
