class InvalidInputError(Exception):
    pass


class CyrillicError(InvalidInputError):
    pass


class CapitalError(InvalidInputError):
    pass


class CharachterError(Exception):
    pass


class BadCharacterError(CharachterError):
    pass


class StartsWithDigitError(CharachterError):
    pass


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


def check_cyrillic(name: str):
    symbol1 = ord("А")
    symbol2 = ord("я")
    if any(symbol1 <= ord(char) <= symbol2 for char in name):
        pass
    else:
        raise CyrillicError


def check_capital(name: str):
    if name.istitle():
        pass
    else:
        raise CapitalError


def name_validation(name: str):
    if not isinstance(name, str):
        raise TypeError

    check_cyrillic(name)
    check_capital(name)

    return name


def user_validation(**kwargs):
    default_keys = {"last_name", "first_name", "username"}
    if kwargs.keys() != default_keys:
        raise KeyError
    name_validation(kwargs["last_name"])
    name_validation(kwargs["first_name"])
    username_validation(kwargs["username"])

    return kwargs


if __name__ == "__main__":
    print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45"))
