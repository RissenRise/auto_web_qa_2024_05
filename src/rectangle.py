from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b, name):
        super().__init__(name="Rectangle")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Введенные числа не должны быть отрицательными")
        self.side_a = side_a
        self.side_b = side_b
        self.name = name

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()

r = Rectangle(10, 20, "Rectangle")
print(r.get_perimeter)
print(r.get_area)