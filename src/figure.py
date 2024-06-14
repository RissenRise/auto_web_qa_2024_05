from abc import ABC, abstractmethod


class Figure(ABC):
    """ Класс используется для вычисления параметров геометрических фигур"""

    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def get_area(self):
        pass

    @property
    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Input must be a geometric figure")
        return self.get_area() + other_figure.get_area()
