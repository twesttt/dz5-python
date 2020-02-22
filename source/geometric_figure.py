from abc import ABC, abstractmethod, abstractproperty
import math


class GeometricFigure:
    __angles = None

    def __init__(self, name, angles):
        self.name = name
        self.__angles = angles

    def get_angles(self):
        return self.__angles

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_square(self, other_figure):
        if isinstance(other_figure, GeometricFigure):
            return self.get_area() + other_figure.get_area()
        else:
            raise AttributeError("Передан инстанс неверного класса")


class Triangle(GeometricFigure):
    _vertex1 = None
    _vertex2 = None
    _vertex3 = None

    def __init__(self, name, a, b, c):
        super().__init__(name, 3)
        self._vertex1 = a
        self._vertex2 = b
        self._vertex3 = c

        self._side1_length = math.sqrt(
            (self._vertex1[0] - self._vertex2[0]) ** 2 + (self._vertex1[1] - self._vertex2[1]) ** 2)
        self._side2_length = math.sqrt(
            (self._vertex2[0] - self._vertex3[0]) ** 2 + (self._vertex2[1] - self._vertex3[1]) ** 2)
        self._side3_length = math.sqrt(
            (self._vertex3[0] - self._vertex1[0]) ** 2 + (self._vertex3[1] - self._vertex1[1]) ** 2)

        check1 = (self._side1_length + self._side2_length) <= self._side3_length
        check2 = (self._side2_length + self._side3_length) <= self._side1_length
        check3 = (self._side3_length + self._side1_length) <= self._side2_length

        if check1 or check2 or check3:
            raise AttributeError("Неверно заданы вершины треугольника")

    def get_area(self):
        """ Высчитываем площадь по формуле Герона, зная только 3 стороны"""
        p = self.get_perimeter() / 2
        sq = math.sqrt(p * (p - self._side1_length) * (p - self._side2_length) * (p - self._side3_length))
        return sq

    def get_perimeter(self):
        return self._side1_length + self._side2_length + self._side3_length


class Rectangle(GeometricFigure):
    _side1_length = None
    _side2_length = None

    def __init__(self, name, a, b, c, d):
        super().__init__(name, 4)
        self._vertex1 = a
        self._vertex2 = b
        self._vertex3 = c
        self._vertex4 = d

        """Проверяем, что стороны прямоугольника параллельны осям"""
        check1 = (self._vertex1[0] == self._vertex2[0])
        check2 = (self._vertex2[1] == self._vertex3[1])
        check3 = (self._vertex3[0] == self._vertex4[0])
        check4 = (self._vertex4[1] == self._vertex1[1])

        if not (check1 and check2 and check3 and check4):
            raise AttributeError("Неверно заданы вершины прямоугольника")

        self._side1_length = self._vertex2[1] - self._vertex1[1]
        self._side2_length = self._vertex4[0] - self._vertex1[0]

    def get_area(self):
        return self._side1_length * self._side2_length

    def get_perimeter(self):
        return (self._side1_length + self._side2_length) * 2


class Foursquare(Rectangle):
    """ Проверяем, что фигура - квадрат"""

    def __init__(self, name, a, b, c, d):
        super().__init__(name, a, b, c, d)

        if self._side1_length != self._side2_length:
            raise AttributeError("Это не квадрат!")


class Circle(GeometricFigure):
    _center = None
    _radius = None

    def __init__(self, name, center, radius):
        super().__init__(name, 0)
        self._center = center
        self._radius = radius

        if self._radius <= 0:
            raise AttributeError("Неверно задан радиус!")

    def get_area(self):
        return math.pi * (self._radius ** 2)

    def get_perimeter(self):
        return self._radius * 2
