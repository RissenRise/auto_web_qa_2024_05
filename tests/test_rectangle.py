from src.rectangle import Rectangle
import pytest


def test_rectangle_area_with_known_sides():
    r = Rectangle(3, 5, "Rectangle")
    assert r.get_area == 15


def test_rectangle_perimeter_with_known_sides():
    r = Rectangle(3, 5, "Rectangle")
    assert r.get_perimeter == 16


def test_rectangle_area_with_different_known_sides():
    r = Rectangle(4, 6, "Rectangle")
    assert r.get_area == 24


def test_rectangle_perimeter_with_different_known_sides():
    r = Rectangle(4, 6, "Rectangle")
    assert r.get_perimeter == 20


def test_rectangle_creation_with_missing_side():
    with pytest.raises(TypeError):
        r = Rectangle(3)


def test_rectangle_creation_with_negative_side():
    with pytest.raises(ValueError):
        r = Rectangle(-3, 5, "Rectangle")


def test_rectangle_creation_with_zero_side():
    with pytest.raises(ValueError):
        r = Rectangle(0, 5, "Rectangle")


def test_rectangle_creation_with_non_numeric_side():
    with pytest.raises(TypeError):
        r = Rectangle("3", 5, "Rectangle")
