def same_type(func):

    def wrapper(*args):
        state = 0
        for i in range(len(args) - 1):
            if not isinstance(args[i + 1], type(args[i])):
                state = 1
                break
        if state == 0:
            return func(*args)
        else:
            print("Обнаружены различные типы данных")
            return False

    return wrapper
