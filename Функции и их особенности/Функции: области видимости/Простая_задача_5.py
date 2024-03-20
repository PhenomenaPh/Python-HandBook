def is_prime(x: int) -> bool:
    delim = 2

    while delim**2 <= x and x % delim != 0:
        delim += 1

    if delim**2 > x:
        return True
    else:
        return False
