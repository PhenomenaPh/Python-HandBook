def number_length(number: int) -> int:
    num = 0

    for val in str(number):
        if val.isdigit():
            num += 1

    return num
