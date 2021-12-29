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



    class PointFactory:

        def new_cartesian_point(self, x, y):
            return Point(x, y)


        def new_polar_point(self, rho, theta):
            return Point(rho * sin(theta), rho * cos(theta))

    
    factory = PointFactory()



if __name__ == '__main__':
    p = Point.factory.new_polar_point(2, 3)
    p2 = Point.factory.new_cartesian_point(1,3)

    print(p)
    print(p2)