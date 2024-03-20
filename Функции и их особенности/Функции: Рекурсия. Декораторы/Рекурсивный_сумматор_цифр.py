def recursive_digit_sum(num: str) -> int:
    num = str(num)
    if len(num) == 1:
        return int(num)
    else:
        return int(num[0]) + recursive_digit_sum(num[1:])
