import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__(radius)
        if radius <= 0:
            raise ValueError("Введенные числа не должны быть отрицательными")
        if not isinstance(radius, (int, float)):
            raise TypeError("Введите число")
        self.radius = radius

    @property
    def get_area(self):
        return math.pi * (self.radius ** 2)

    @property
    def get_perimeter(self):
        return 2 * math.pi * self.radius

