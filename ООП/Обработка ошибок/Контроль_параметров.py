def only_positive_even_sum(a: int, b: int):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Вызвано исключение TypeError")
    if not (a % 2 == 0 and a > 0) or not (b % 2 == 0 and b > 0):
        raise ValueError("Вызвано исключение ValueError")

    return a + b


# print(only_positive_even_sum("3", 2.5))
print(only_positive_even_sum(-5, 4))
