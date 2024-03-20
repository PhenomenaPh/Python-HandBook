def answer(f):

    def wrapper(*args, **kwargs):
        return f"Результат функции: {f(*args, **kwargs)}"

    return wrapper
