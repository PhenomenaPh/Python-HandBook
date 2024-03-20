class Rectangle:
    """
    На вход поступают два противоположных угла прямоугольника в виде tuple

    get_pos() — возвращает координаты верхнего левого угла в виде кортежа;
    get_size() — возвращает размеры в виде кортежа;
    move(dx, dy) — изменяет положение на заданные значения;
    resize(width, height) — изменяет размер
    """

    def __init__(self, point1, point2):
        self.lower_left = [
            min(point1[0], point2[0]),
            min(point1[1], point2[1]),
        ]
        self.upper_right = [
            max(point1[0], point2[0]),
            max(point1[1], point2[1]),
        ]

    def get_pos(self):
        return (round(self.lower_left[0], 2), round(self.upper_right[1], 2))

    def get_size(self):
        self.width = round(self.upper_right[0] - self.lower_left[0], 2)
        self.height = round(self.upper_right[1] - self.lower_left[1], 2)

        return (round(self.width, 2), round(self.height, 2))

    def area(self):
        width = round(self.upper_right[0] - self.lower_left[0], 2)
        height = round(self.upper_right[1] - self.lower_left[1], 2)
        return round(width * height, 2)

    def perimeter(self):
        width = round(self.upper_right[0] - self.lower_left[0], 2)
        height = round(self.upper_right[1] - self.lower_left[1], 2)
        return round(2 * (width + height), 2)

    def move(self, dx, dy):
        self.lower_left[0] = round(self.lower_left[0] + dx, 2)
        self.lower_left[1] = round(self.lower_left[1] + dy, 2)

        self.upper_right[0] = round(self.upper_right[0] + dx, 2)
        self.upper_right[1] = round(self.upper_right[1] + dy, 2)

    def resize(self, width, height):
        self.upper_right[0] = round(self.lower_left[0] + width, 2)
        self.lower_left[1] = round(self.upper_right[1] - height, 2)


rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())
