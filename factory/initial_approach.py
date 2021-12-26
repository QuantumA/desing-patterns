from enum import Enum
from math import sin, cos

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2




class Point:
#    def __init__(self, x, y):
#         self.x = x
#         self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


    # But what if we have different types of points such as polar points or cartesian points? 
    # x and y parameters of the initializer becomes poorly idiomatic for the polar points and
    # we can't have more than one initializer per class. 

    # We can think on create something simmilar to the following initializer but we still having the same
    # problem even worst with the parameters. Also this solution violates the Open-Close principle.


    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * sin(b)
            self.y = a * cos(b)