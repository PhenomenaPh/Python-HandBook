def make_matrix(size: tuple | int, value: int = 0) -> list:
    if isinstance(size, tuple):
        return [[value for i in range(size[0])] for j in range(size[1])]
    else:
        return [[value for i in range(size)] for j in range(size)]
