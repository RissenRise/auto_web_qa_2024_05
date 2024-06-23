from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b, name):
        super().__init__(name="Rectangle")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Введенные числа не должны быть отрицательными")
        elif side_a is None or side_b is None:
            raise ValueError("Нужно передать обе стороны")
        elif not isinstance(side_a, (int, float)) or side_a <= 0:
            raise ValueError("side_a must be a positive number")
        elif not isinstance(side_b, (int, float)) or side_b <= 0:
            raise ValueError("side_b must be a positive number")
        elif not isinstance(name, str):
            raise TypeError("name must be a string")
        self.side_a = side_a
        self.side_b = side_b
        self.name = name



    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)

        try:
            r = Rectangle(3)
        except ValueError as e:
            print(f"Ошибка значения: {e}")
        except TypeError as e:
            print(f"Ошибка типа: {e}")