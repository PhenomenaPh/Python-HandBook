from typing import Union


class Fraction:
    def __init__(self, *args):
        if len(args) == 2:
            self._numerator, self._denominator = self._assign_fraction_parts(args)
        else:
            if "/" in str(args[0]):
                values = list(map(int, args[0].split("/")))
                self._numerator, self._denominator = self._assign_fraction_parts(values)
            else:
                self._numerator, self._denominator = int(args[0]), 1
        self._fractionate()

    @staticmethod
    def _assign_fraction_parts(values):
        if values[0] * values[1] < 0:
            return -abs(values[0]), abs(values[1])
        else:
            return abs(values[0]), abs(values[1])

    def _fractionate(self):
        temp_a, temp_b = abs(self._numerator), abs(self._denominator)

        while temp_b:
            temp_a, temp_b = temp_b, temp_a % temp_b

        if (self._numerator < 0) and (self._denominator < 0):
            self._numerator *= -1
            self._denominator *= -1

        self._numerator //= temp_a
        self._denominator //= temp_a

    def numerator(self, value=None):
        if value is not None:
            self._numerator = value * (self._numerator // abs(self._numerator))
            self._fractionate()
        return abs(self._numerator)

    def denominator(self, value=None):
        if value is not None:
            self._denominator = value
            self._fractionate()
        return abs(self._denominator)

    def reverse(self):
        return Fraction(self._denominator, self._numerator)

    def __neg__(self):
        return Fraction(-self._numerator, self._denominator)

    #
    def __str__(self) -> str:
        if self._denominator * self._numerator < 0:
            return f"-{abs(self._numerator)}/{abs(self._denominator)}"
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self) -> str:
        if self._denominator * self._numerator < 0:
            return f"Fraction('-{abs(self._numerator)}/{abs(self._denominator)}')"
        return f"Fraction('{self._numerator}/{self._denominator}')"

    def __add__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        denominator = self._denominator * other._denominator
        numerator = (
            self._numerator * other._denominator + other._numerator * self._denominator
        )
        return Fraction(numerator, denominator)

    def __radd__(self, other: Union["Fraction"]):
        if isinstance(other, int):
            other = Fraction(other)
        denominator = self._denominator * other._denominator
        numerator = (
            self._numerator * other._denominator + other._numerator * self._denominator
        )
        return Fraction(numerator, denominator)

    def __sub__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        denominator = self._denominator * other._denominator
        numerator = (
            self._numerator * other._denominator - other._numerator * self._denominator
        )
        return Fraction(numerator, denominator)

    def __rsub__(self, other: Union["Fraction"]):
        if isinstance(other, int):
            other = Fraction(other)
        denominator = self._denominator * other._denominator
        numerator = (
            other._numerator * self._denominator - self._numerator * other._denominator
        )
        return Fraction(numerator, denominator)

    def __iadd__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        self._numerator = (
            self._numerator * other._denominator + other._numerator * self._denominator
        )
        self._denominator *= other._denominator
        self._fractionate()
        return self

    def __isub__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        self._numerator = (
            self._numerator * other._denominator - other._numerator * self._denominator
        )
        self._denominator *= other._denominator
        self._fractionate()
        return self

    def __mul__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        numerator = self._numerator * other._numerator
        denominator = self._denominator * other._denominator
        return Fraction(numerator, denominator)

    def __rmul__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        numerator = self._numerator * other._numerator
        denominator = self._denominator * other._denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        numerator = self._numerator * other._denominator
        denominator = self._denominator * other._numerator
        return Fraction(numerator, denominator)

    def __rtruediv__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        numerator = other._numerator * self._denominator
        denominator = other._denominator * self._numerator
        return Fraction(numerator, denominator)

    def __imul__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        self._numerator *= other._numerator
        self._denominator *= other._denominator
        self._fractionate()
        return self

    def __itruediv__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        self._numerator *= other._denominator
        self._denominator *= other._numerator
        self._fractionate()
        return self

    def __gt__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        return (self._numerator / self._denominator) > (
            other._numerator / other._denominator
        )

    def __lt__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        return (self._numerator / self._denominator) < (
            other._numerator / other._denominator
        )

    def __le__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        return (self._numerator / self._denominator) <= (
            other._numerator / other._denominator
        )

    def __ge__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        return (self._numerator / self._denominator) >= (
            other._numerator / other._denominator
        )

    def __eq__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        return (self._numerator / self._denominator) == (
            other._numerator / other._denominator
        )

    def __ne__(self, other: Union["Fraction", int]):
        if isinstance(other, int):
            other = Fraction(other)
        return not self.__eq__(other)


if __name__ == "__main__":
    pass
