class NameError(Exception):
    pass


class CyrillicError(NameError):
    pass


class CapitalError(NameError):
    pass


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


if __name__ == "__main__":
    print(name_validation("user"))
