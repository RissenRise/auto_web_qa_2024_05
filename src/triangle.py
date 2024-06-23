from abc import ABC

from src.figure import Figure


class Triangle(Figure, ABC):
    def __init__(self, side_a, side_b, side_c, name):
        super().__init__(name="Triangle")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Введенные числа не должны быть отрицательными")
        elif side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("Сумма двух сторон треугольника должна быть больше третьей")
        elif side_a is None or side_b is None or side_c is None:
            raise TypeError("Нужно передать три стороны")
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

