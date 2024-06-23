from src.rectangle import Rectangle
from src.figure import Figure


class Square(Rectangle):
    def __init__(self, side_a, name):
        super().__init__(side_a=side_a, side_b=side_a, name='Square')
        if side_a <= 0:
            raise ValueError("Введенные числа не должны быть отрицательными")
        elif not isinstance(side_a, (int, float)):
            raise ValueError("Введите число, а не строку")
        elif side_a is None:
            raise ValueError("Нужно передать значение стороны")
        elif not isinstance(name, str):
            raise TypeError("Нужно передать строку")


    @property
    def get_area(self):
        return self.side_a ** 2

    @property
    def get_perimeter(self):
        return 4 * self.side_a