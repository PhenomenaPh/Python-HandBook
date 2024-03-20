def recursive_sum(*args):
    if len(args) == 1:
        return args[0]
    else:
        return recursive_sum(*args[1::]) + args[0]
