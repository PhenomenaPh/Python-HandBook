def fibonacci(num: int):
    a, b = 0, 1

    for i in range(num):
        yield a
        a, b = b, a + b
