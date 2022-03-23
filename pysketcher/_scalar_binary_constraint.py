from abc import ABC
from typing import Any

from ._abstract_scalar import _AbstractScalar
from ._scalar_constraint import ScalarConstraint


class ScalarBinaryConstraint(ScalarConstraint, ABC):
    """A Constraint which applies to a Scalar and accepts two Scalar Parameters."""

    def __init__(self, s1, s2):
        arg_dict = {
            "First argument": s1,
            "Second argument": s2,
        }
        for name, arg in arg_dict.items():
            if not isinstance(arg, (_AbstractScalar, int, float)):
                raise TypeError(
                    f"{name} must be a Scalar, "
                    f"int or float; not a {arg.__class__.__name__}."
                )
        self._s1 = s1
        self._s2 = s2

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self._s1 is other._s1 and self._s2 is other._s2

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}<{self._s1}, {self._s2}>"
