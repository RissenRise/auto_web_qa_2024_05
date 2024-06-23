from src.square import Square
import pytest


def test_square_creation_with_positive_side():
    s = Square(5, "Square")
    assert s.side_a == 5
    assert s.name == "Square"


def test_square_get_area():
        s = Square(5, "Square")
        assert s.get_area == 25


def test_square_perimeter():
    s = Square(5, "Square")
    assert s.get_perimeter == 20


def test_square_creation_with_negative_side():
    with pytest.raises(ValueError):
        s = Square(-5, "Square")


def test_square_creation_with_zero_side():
    with pytest.raises(ValueError):
        s = Square(0, "Square")


def test_square_str():
    with pytest.raises(TypeError):
        s = Square("5", "Square")