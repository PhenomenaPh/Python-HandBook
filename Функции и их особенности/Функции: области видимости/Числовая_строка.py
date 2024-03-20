def split_numbers(numbers: str) -> list:
    numbers = tuple(map(int, numbers.split()))

    return numbers
