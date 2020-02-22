import pytest
from source.geometric_figure import *


def test_create_triangle():
    """Проверяем, выпадет ли ошибка, если неверно указаны вершнины"""
    with pytest.raises(AttributeError):
        my_triangle = Triangle(name="triangle1", a=[0, 0], b=[0, 3], c=[0, 1])


def test_get_area():
    """Проверяем, что геттер площади работает верно"""

    my_triangle = Triangle(name="triangle1", a=[0, 0], b=[0, 2], c=[2, 0])

    assert my_triangle.get_area() == 1.9999999999999993


def test_get_perimeter():
    """Проверяем, что геттер периметра работает верно"""

    my_triangle = Triangle(name="triangle1", a=[0, 0], b=[0, 2], c=[2, 0])
    assert my_triangle.get_perimeter() == 6.82842712474619


def test_add_area():
    """Проверяем, что геттер периметра работает верно"""

    my_circle = Circle(name="circle1", center=[0, 3], radius=2)
    my_triangle = Triangle(name="triangle1", a=[0, 0], b=[0, 2], c=[2, 0])
    my_circle_area = my_circle.get_area()
    my_triangle_area = my_triangle.get_area()
    assert my_triangle.add_square(my_circle) == (my_circle_area + my_triangle_area)


def test_add_area_of_wrong_object():
    """Проверяем, что нельзя сложить площади, если другой объект не является геометрической фигурой"""
    with pytest.raises(AttributeError):
        my_circle = "five"
        my_triangle = Triangle(name="triangle1", a=[0, 0], b=[0, 2], c=[2, 0])
        my_triangle_area = my_triangle.add_square(my_circle)