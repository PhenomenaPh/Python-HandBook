class CharachterError(Exception):
    pass


class BadCharacterError(CharachterError):
    pass


class StartsWithDigitError(CharachterError):
    pass


# Checking if first character is a digit
def check_first_digit(name: str):
    if name[0].isdigit():
        raise StartsWithDigitError
    else:
        pass


def allowed_characters(name: str):
    chars_range = (ord("A"), ord("z"))

    if not all(
        chars_range[0] <= ord(char) <= chars_range[1] or char == "_" or char.isdigit()
        for char in name
    ):
        raise BadCharacterError
    else:
        pass


def username_validation(name: str):
    if not isinstance(name, str):
        raise TypeError

    allowed_characters(name)
    check_first_digit(name)

    return name
