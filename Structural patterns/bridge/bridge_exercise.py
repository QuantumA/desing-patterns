from abc import ABC
import unittest

class Shape(ABC):
    def __init__(self, renderer, name):
        self.renderer = renderer
        self.name = name

    def __str__(self):
        return 'Drawing %s as %s' % (self.name, self.renderer.what_to_render_as)


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Triangle')


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Square')


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None
class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'pixels'


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'lines'


class RasterRender(Renderer):
    def __str__(self):
        return f'Drawing {self.name} as pixels'

class Evaluate(unittest.TestCase):
    def test_square_vector(self):
        sq = Square(VectorRenderer())
        self.assertEqual(str(sq), 'Drawing Square as lines')

    def test_pixel_triangle(self):
        tr = Triangle(RasterRenderer())
        self.assertEqual(str(tr), 'Drawing Triangle as pixels')


if __name__ == '__main__':

    Evaluate().test_pixel_triangle()
    Evaluate().test_square_vector()
