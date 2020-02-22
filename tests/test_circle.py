import pytest
from source.geometric_figure import *


def test_create_circle():
    """Проверяем, выпадет ли ошибка, если радиус указан неверно"""
    with pytest.raises(AttributeError):
        my_circle = Circle(name="circle1", center=[0, 3], radius=0)


def test_get_angles():
    """Проверяем, что количество углов должно быть равным нулю"""

    my_circle = Circle(name="circle1", center=[0, 3], radius=2)
    assert my_circle.get_angles() == 0


def test_get_area():
    """Проверяем, что геттер площади работает верно"""

    my_circle = Circle(name="circle1", center=[0, 3], radius=2)
    area = math.pi * (2 ** 2)
    assert area == my_circle.get_area()


def test_get_perimeter():
    """Проверяем, что геттер периметра работает верно"""

    my_circle = Circle(name="circle1", center=[0, 3], radius=2)
    assert my_circle.get_perimeter() == 4


def test_add_area():
    """Проверяем, что геттер периметра работает верно"""

    my_circle = Circle(name="circle1", center=[0, 3], radius=2)
    my_rectangle = Rectangle(name="rectangle1", a=[0, 0], b=[0, 3], c=[2, 3], d=[2, 0])
    my_circle_area = my_circle.get_area()
    my_rectangle_area = my_rectangle.get_area()
    assert my_circle.add_square(my_rectangle) == (my_circle_area + my_rectangle_area)


def test_get_name():
    """Проверяем, что у фигуры есть имя"""

    my_circle = Circle(name="circle1", center=[0, 3], radius=2)
    assert my_circle.name == "circle1"
