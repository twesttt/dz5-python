import pytest
from source.geometric_figure import *


def test_create_rectangle():
    """Проверяем, выпадет ли ошибка, если неверно указаны вершнины"""
    with pytest.raises(AttributeError):
        my_circle = Rectangle(name="rectangle1", a=[0, 1], b=[0, 3], c=[2, 3], d=[2, 0])


def test_get_area():
    """Проверяем, что геттер площади работает верно"""

    my_rectangle = Rectangle(name="rectangle1", a=[0, 0], b=[0, 3], c=[2, 3], d=[2, 0])
    assert my_rectangle.get_area() == 6


def test_get_perimeter():
    """Проверяем, что геттер периметра работает верно"""

    my_rectangle = Rectangle(name="rectangle1", a=[0, 0], b=[0, 3], c=[2, 3], d=[2, 0])
    assert my_rectangle.get_perimeter() == 10


def test_add_area():
    """Проверяем, что геттер периметра работает верно"""

    my_circle = Circle(name="circle1", center=[0, 3], radius=2)
    my_rectangle = Rectangle(name="rectangle1", a=[0, 0], b=[0, 3], c=[2, 3], d=[2, 0])
    my_circle_area = my_circle.get_area()
    my_rectangle_area = my_rectangle.get_area()
    assert my_rectangle.add_square(my_circle) == (my_circle_area + my_rectangle_area)


def test_add_area_of_wrong_object():
    """Проверяем, что нельзя сложить площади, если другой объект не является геометрической фигурой"""
    with pytest.raises(AttributeError):
        my_circle = 5
        my_rectangle = Rectangle(name="rectangle1", a=[0, 0], b=[0, 3], c=[2, 3], d=[2, 0])
        my_rectangle_area = my_rectangle.add_square(my_circle)


