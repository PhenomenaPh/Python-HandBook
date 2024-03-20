class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = self.x + new_x
        self.y = self.y + new_y

    def length(self, new_point):
        length_x = (new_point.x - self.x) ** 2
        length_y = (new_point.y - self.y) ** 2

        return round((length_x + length_y) ** (1 / 2), 2)


class PatchedPoint(Point):
    def __init__(self, *args) -> None:
        if args:
            if isinstance(args[0], tuple):
                self.x, self.y = args[0]
            else:
                self.x, self.y = args
        else:
            self.x, self.y = 0, 0

    def __str__(self) -> str:
        return f"{(self.x, self.y)}"

    def __repr__(self) -> str:
        return f"PatchedPoint{(self.x, self.y)}"

    def __add__(self, other):
        if isinstance(other, tuple):
            return PatchedPoint(self.x + other[0], self.y + other[1])
        else:
            raise ValueError("You can only add PatchedPoint to tuple")

    def __iadd__(self, other):
        if isinstance(other, tuple):
            self.x += other[0]
            self.y += other[1]
            return self
        else:
            raise ValueError("You can only add PatchedPoint to tuple")


first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)
