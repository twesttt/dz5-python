import pytest
from source.geometric_figure import *


def test_create_foursquare():
    """Проверяем, выпадет ли ошибка, если неверно указаны вершнины"""
    with pytest.raises(AttributeError):
        my_circle = Foursquare(name="foursquare1", a=[0, 1], b=[0, 3], c=[2, 3], d=[2, 0])


def test_get_area():
    """Проверяем, что геттер площади работает верно"""

    my_foursquare = Foursquare(name="rectangle1", a=[0, 0], b=[0, 2], c=[2, 2], d=[2, 0])
    assert my_foursquare.get_area() == 4


def test_get_perimeter():
    """Проверяем, что геттер периметра работает верно"""

    my_foursquare = Foursquare(name="rectangle1", a=[0, 0], b=[0, 2], c=[2, 2], d=[2, 0])
    assert my_foursquare.get_perimeter() == 8


def test_add_area():
    """Проверяем, что геттер периметра работает верно"""

    my_circle = Circle(name="circle1", center=[0, 3], radius=2)
    my_foursquare = Foursquare(name="rectangle1", a=[0, 0], b=[0, 2], c=[2, 2], d=[2, 0])
    my_circle_area = my_circle.get_area()
    my_foursquare_area = my_foursquare.get_area()
    assert my_foursquare.add_square(my_circle) == (my_circle_area + my_foursquare_area)


def test_get_name():
    """Проверяем, что у фигуры есть имя"""

    my_foursquare = Foursquare(name="rectangle1", a=[0, 0], b=[0, 2], c=[2, 2], d=[2, 0])
    assert my_foursquare.name == "rectangle1"
