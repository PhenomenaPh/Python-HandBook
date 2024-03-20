class Rectangle:

    def __init__(self, x, y):
        # Инициализируем верхнюю левую точку
        self.left_upper = [min(x[0], y[0]), max(x[1], y[1])]

        # Рассчитываем длинну и ширину
        self.width = max(x[0], y[0]) - self.left_upper[0]
        self.heigth = self.left_upper[1] - min(x[1], y[1])

    def perimeter(self):
        return round(2 * (self.width + self.heigth), 2)

    def area(self):
        return round(self.width * self.heigth, 2)

    def get_pos(self):
        return round(self.left_upper[0], 2), round(self.left_upper[1], 2)

    def get_size(self):
        return round(self.width, 2), round(self.heigth, 2)

    def move(self, dx, dy):
        self.left_upper[0] += dx
        self.left_upper[1] += dy

    def resize(self, width, height):
        self.width = width
        self.heigth = height

    def turn(self):

        center = (
            self.left_upper[0] + self.width / 2,
            self.left_upper[1] - self.heigth / 2,
        )

        self.left_upper = [center[0] - self.heigth / 2, center[1] + self.width / 2]
        self.heigth, self.width = self.width, self.heigth

    def scale(self, factor):
        center = (
            self.left_upper[0] + self.width / 2,
            self.left_upper[1] - self.heigth / 2,
        )

        self.left_upper = (
            center[0] - round(self.width * factor, 2) / 2,
            center[1] + round(self.heigth * factor, 2) / 2,
        )

        self.width = round(self.width * factor, 2)
        self.heigth = round(self.heigth * factor, 2)


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep="\n")
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep="\n")
