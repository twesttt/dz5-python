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


class Triangle(GeometricFigure):
    _side1_length = None
    _side2_length = None
    _side3_length = None

    def __init__(self, name, a, b, c):
        super().__init__(name, 3)
        self._side1_length = a
        self._side2_length = b
        self._side3_length = c

    def get_area(self):
        """ Высчитываем площадь по формуле Герона, зная только 3 стороны"""
        p = self.get_perimeter() / 2
        sq = math.sqrt(p * (p - self._side1_length) * (p - self._side2_length) * (p - self._side3_length))
        return sq

    def get_perimeter(self):
        return self._side1_length + self._side2_length + self._side3_length

    def set_sides_length(self, a, b, c):
        self._side1_length = a
        self._side2_length = b
        self._side3_length = c


class Rectangle(GeometricFigure):
    _side_length = None

    def __init__(self, name, a):
        super().__init__(name, 4)
        self._side_length = a

    def get_area(self):
        return self._side_length ** 2


# my_triangle = Triangle(name="My_triangle", a=5, b=3, c=5)
# print(my_triangle.get_perimeter())
# print(my_triangle.get_area())
# print(my_triangle.get_angles())

class Rectangle(GeometricFigure):
    _side_length = None

    def __init__(self, name, a):
        super().__init__(name, 4)
        self._side_length = a

    def get_area(self):
        return self._side_length ** 2
