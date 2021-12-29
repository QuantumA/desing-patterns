from enum import Enum
from math import sin, cos

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2




class Point:
    def __init__(self, x, y):
         self.x = x
         self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))


# If the number of ways to initialize the point becomes higher, then outsource them to other entity becomes a good option.
# check outsourcing_factory.py


if __name__ == '__main__':
    p = Point(2, 3)
    p2 = p.new_polar_point(1,3)

    