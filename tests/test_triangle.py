from src.triangle import Triangle
import pytest
import math


def test_triangle_area_with_known_sides():
    a, b, c = 10, 10, 15
    t = Triangle(a, b, c, "Triangle")
    s = (a + b + c) / 2  # полупериметр
    expected_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    assert abs(t.get_area - expected_area) < 1e-9  # очень маленький допуск


def test_triangle_perimeter_with_known_sides():
    t = Triangle(10, 10, 10, "Rectangle")
    assert t.get_perimeter == 30


def test_triangle_area_with_known_sides_negative():
    with pytest.raises(ValueError):
        a, b, c = 3, 5, 10
        t = Triangle(a, b, c, "Triangle")
        s = (a + b + c) / 2  # полупериметр
        expected_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        assert abs(t.get_area - expected_area) < 1e-9  # очень маленький допуск


def test_triangle_creation_with_one_missing_side():
    with pytest.raises(TypeError):
        t = Triangle(3, 5, name='Triangle')


def test_triangle_creation_with_negative_len_side():
    with pytest.raises(ValueError):
        t = Triangle(-3, 15, 10, name="Triangle")


def test_triangle_creation_with_zero_side():
    with pytest.raises(ValueError):
        t = Triangle(0, 5, 10, name="Triangle")


def test_triangle_creation_with_non_numeric_side():
    with pytest.raises(TypeError):
        t = Triangle("3", 5, 10, "Triangle")
