import logging

import numpy as np
import scipy.optimize as spo
import sympy as sp

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# def gradient(x1: float, x2: float, y1: float, y2: float):
#     if x1 == x2:
#         return math.inf
#     return (y2 - y1) / (x2 - x1)

class LinearDistanceConstraint:
    def __init__(self, x0, y0, d):
        self._d2 = d**d
        self._x0 = x0
        self._y0 = y0
    
    def error(self, x: np.array) -> float:
        x1 = x[0]
        y1 = x[1]

        return ((x1 - self._x0)**2 + (y1 - self._y0)**2) - self._d2

    def jacobian(self, x: np.array):
        x1 = x[0]
        y1 = x[1]

        return 2*x1 - 2*self._x0, 2*y1 - 2*self._y0

class Main:
    def run(self):
        log.info("The BFGS application has started.")

        # x0, y0, x1, y1, d = sp.symbols("x0 y0 x1 y1 d")
        # ldc = LinearDistanceConstraint(x0, y0, d)
        # f = sp.Matrix([ldc.error(np.array([x1, y1]))])

        # print(f.jacobian([x1, y1]))

        p1x = 0
        p1y = 0

        p2x = 0
        p2y = 5

        d = 3

        ldc1 = LinearDistanceConstraint(p1x, p1y, d)
        ldc2 = LinearDistanceConstraint(p2x, p2y, d)

        def error(x: np.array):
            return np.array([ldc1.error(x), ldc2.error(x)])
        
        def jacobian(x: np.array):
            return np.array([ldc1.jacobian(x), ldc2.jacobian(x)])

        result = spo.root(lambda x: (error(x), jacobian(x)), np.array([1.,1.]), jac=True)
        print(result)



if __name__ == "__main__":
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logging.getLogger().addHandler(ch)
    Main().run()