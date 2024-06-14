from abc import ABC

from src.figure import Figure


class Triangle(Figure, ABC):
    def __init__(self, side_a, side_b, side_c, name):
        super().__init__(name="Triangle")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Введенные числа не должны быть отрицательными")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = name

    @property
    def get_area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()


t = Triangle(10, 10, 15, "Triangle")
print(t.get_perimeter)
print(t.get_area)
