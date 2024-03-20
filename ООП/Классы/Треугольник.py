class Rectangle:
    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2

    def _calculate_sides(self):
        # Рассчитываем длины сторон прямоугольника
        a = abs(self.point1[0] - self.point2[0])
        b = abs(self.point1[1] - self.point2[1])
        return a, b

    def perimeter(self):
        a, b = self._calculate_sides()
        return round((a + b) * 2, 2)

    def area(self):
        a, b = self._calculate_sides()
        return round(a * b, 2)


rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())
