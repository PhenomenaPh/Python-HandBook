class NumbersError(Exception):
    pass


class InfiniteSolutionsError(NumbersError):
    pass


class NoSolutionsError(NumbersError):
    pass


def check_rational(number):
    if not isinstance(number, (int, float)):
        raise TypeError


def find_roots(a: float, b: float, c: float):
    for i in (a, b, c):
        check_rational(i)
    discriminant = b**2 - 4 * a * c

    if a == 0:
        if b == 0:
            if c == 0:
                raise InfiniteSolutionsError(
                    "Вызвано исключение InfiniteSolutionsError "
                )
            else:
                raise NoSolutionsError("Вызывано исключение NoSolutionError")
        else:
            return -c / b, -c / b  # Returning a tuple with one element

    if discriminant < 0:
        raise NoSolutionsError("Вызывано исключение NoSolutionError")

    elif discriminant == 0:
        return -b / (2 * a), -b / (2 * a)
    else:
        square_root = discriminant**0.5
        root_1 = (-b + square_root) / (2 * a)
        root_2 = (-b - square_root) / (2 * a)

        return min(root_1, root_2), max(root_2, root_1)


print(find_roots(1, 5, 1))
