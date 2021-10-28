from ._abstract_scalar import _AbstractScalar
from ._additive_constraint import AdditiveConstraint
from ._divisive_constraint import DivisiveConstraint
from ._multiplicative_constraint import MultiplicativeConstraint
from ._subtractive_constraint import SubtractiveConstraint


class Scalar(_AbstractScalar):
    """A concrete implementation of a constrained scalar."""

    def __add__(self, other):
        s = self.__class__()
        try:
            s.constrain_with(AdditiveConstraint(self, other))
        except TypeError:
            return NotImplemented
        return s

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        s = self.__class__()
        try:
            s.constrain_with(SubtractiveConstraint(self, other))
        except TypeError:
            return NotImplemented
        return s

    def __truediv__(self, other):
        s = self.__class__()
        try:
            s.constrain_with(DivisiveConstraint(self, other))
        except TypeError:
            return NotImplemented
        return s

    def __mul__(self, other):
        s = self.__class__()
        try:
            s.constrain_with(MultiplicativeConstraint(self, other))
        except TypeError:
            return NotImplemented
        return s

    def __rmul__(self, other):
        return self.__mul__(other)
