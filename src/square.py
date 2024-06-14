from src.rectangle import Rectangle
from src.figure import Figure


class Square(Rectangle):
    def __init__(self, side_a, name):
        super().__init__(name='Square')
        self.name = name
        if side_a <= 0:
            raise ValueError("Введенные числа не должны быть отрицательными")

    @property
    def get_area(self):
        return self.side_a ** 2

    @property
    def get_perimeter(self):
        return 4 * self.side_a

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()


s = Square(10, 'Square')
print(s.get_perimeter)
print(s.get_area)
