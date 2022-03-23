import math

import numpy as np
import sympy as sp

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Line:
    def __init__(self, a: float, b: float, c: float):
        # a * x + b * y + c = 0
        self.a = a
        self.b = b
        self.c = c

class LineBuilder:
    @staticmethod
    def from_two_points(p1: Point, p2: Point) -> Line:
        a = p1.y - p2.y
        b = p2.x - p1.x
        c = p1.x * p2.y - p1.y * p2.x
        return Line(a, b, c)

class PerpendicularDistanceConstraint:
    def __init__(self, l: Line, d: float):
        self.l = l
        self.d = d
    
    def error(self, x: np.array):
        x0 = x[0]
        y0 = x[1]

        return abs(self.l.a * x0 + self.l.b * y0 + self.l.c) / sp.sqrt(self.l.a ** 2 + self.l.b ** 2)


class Main:
    def run(self):
        p1x, p1y, p2x, p2y, d = sp.symbols("p1x p1y p2x p2y d")
        x1, y1 = sp.symbols("x1 y1")
        l = LineBuilder.from_two_points(Point(p1x, p1y), Point(p2x,p2y))
        
        pdc = PerpendicularDistanceConstraint(l, d)

        error = pdc.error(np.array([x1, y1]))
        print(sp.diff(error, x1))


if __name__ == '__main__':
    Main().run()