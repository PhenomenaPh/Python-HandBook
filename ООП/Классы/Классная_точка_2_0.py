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


first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
