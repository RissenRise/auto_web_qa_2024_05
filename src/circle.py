import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__(radius)
        if radius <= 0:
            raise ValueError("Введенные числа не должны быть отрицательными")
        self.radius = radius

    @property
    def get_area(self):
        return math.pi * (self.radius ** 2)

    @property
    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()


c = Circle(15)
print(c.get_perimeter)
print(c.get_area)


