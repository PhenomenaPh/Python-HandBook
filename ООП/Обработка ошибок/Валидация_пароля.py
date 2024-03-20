import string
from typing import Callable
import hashlib


class DigitErrors(Exception):
    pass


class MinLengthError(DigitErrors):
    pass


class PossibleCharError(DigitErrors):
    pass


class NeedCharError(DigitErrors):
    pass


def password_validation(
    password: str,
    min_length: int = 8,
    possible_chars: str = string.ascii_letters + string.digits,
    at_least_one: Callable[[str], bool] = str.isdigit,
):

    if not isinstance(password, str):
        raise TypeError

    if len(password) < min_length:
        raise MinLengthError

    if not all(char in possible_chars for char in password):
        raise PossibleCharError

    if not any(at_least_one(char) for char in password):
        raise NeedCharError
    return hashlib.sha256(password.encode()).hexdigest()


if __name__ == "__main__":
    print(password_validation("12345678"))
