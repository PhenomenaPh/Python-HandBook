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


first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
