from abc import ABC
from typing import Any

from ._abstract_scalar import AbstractScalar
from ._scalar_constraint import ScalarConstraint


class ScalarBinaryConstraint(ScalarConstraint, ABC):
    """A Constraint which applies to a Scalar and accepts two Scalar Parameters."""

    def __init__(self, s1, s2):
        if not isinstance(s1, AbstractScalar):
            raise TypeError(
                f"First argument must be a Scalar, not a {s1.__class__.__name__}."
            )
        if not isinstance(s2, (AbstractScalar, int, float)):
            raise TypeError(
                f"Second argument must be a Scalar, int or float; not a {s2.__class__.__name__}."
            )
        self._s1 = s1
        self._s2 = s2

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self._s1 is other._s1 and self._s2 is other._s2
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}<{self._s1, self._s2}>"
