from src.circle import Circle
import pytest
import math


def test_circle_creation_positive():
    c = Circle(radius=20)
    assert c.radius == 20


def test_creation_radius_float():
    c = Circle(radius=5.6)
    assert c.radius == 5.6
    assert c.get_area == math.pi * (c.radius ** 2)


def test_circle_creation_negative():
    with pytest.raises(ValueError):
        c = Circle(radius=-10)


def test_circle_creation_invalid_radius_negative():
    with pytest.raises(TypeError):
        c = Circle(radius="12")


def test_circle_creation_invalid_radius_zero():
    with pytest.raises(ValueError):
        c = Circle(radius=0)