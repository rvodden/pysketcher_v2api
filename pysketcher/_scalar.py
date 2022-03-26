from abc import ABC
from typing import Any

from ._error import InvalidConstraintException
from ._parameter_instance import ParameterInstance
from ._constraint import Constraint


class Scalar(ParameterInstance):
    """A Parameter which can take a scalar value."""

    def __add__(self, other) -> ParameterInstance:
        s = self.__class__()
        try:
            # todo: implement auto naming
            s.constrain_with(AdditiveConstraint("add", s, self, other))
        except TypeError as e:
            print(e)
            return NotImplemented
        return s

    def __radd__(self, other) -> ParameterInstance:
        return self.__add__(other)

    def __sub__(self, other):
        s = self.__class__()
        try:
            # todo: implement auto naming
            s.constrain_with(SubtractiveConstraint("sub", s, self, other))
        except TypeError as e:
            print(e)
            return NotImplemented
        return s

    def __truediv__(self, other):
        s = self.__class__()
        try:
            # todo: implement auto naming
            s.constrain_with(DivisiveConstraint("div", s, self, other))
        except TypeError as e:
            print(e)
            return NotImplemented
        return s

    def __mul__(self, other):
        s = self.__class__()
        try:
            # todo: implement auto naming
            s.constrain_with(MultiplicativeConstraint("mul", s, self, other))
        except TypeError as e:
            print(e)
            return NotImplemented
        return s

    def __rmul__(self, other):
        return self.__mul__(other)


class ScalarConstraint(Constraint, ABC):
    """A constraint which applies to a Scalar."""

    def validate_object(self, instance) -> None:
        if not self._is_scalar(instance):
            raise InvalidConstraintException(
                f"{self.__class__.__name__} can only be applied to"
                f"Scalar, it cannot be applied to  {instance.__class__.__name__}."
            )

    @staticmethod
    def _is_scalar(obj: Any):
        return isinstance(obj, Scalar)


class ScalarBinaryConstraint(ScalarConstraint, ABC):
    """A Constraint which links a Scalar to the value of two other Scalar Parameters."""

    v = Scalar("v")
    s1 = Scalar("s1")
    s2 = Scalar("s2")
    _operator_character = '_'

    # todo: implement auto naming
    def __init__(self, name, v, s1, s2):
        super().__init__(name)
        arg_dict = {
            "First argument": s1,
            "Second argument": s2,
        }
        for name, arg in arg_dict.items():
            if not isinstance(arg, (Scalar, int, float)):
                raise TypeError(
                    f"{name} must be a Scalar, "
                    f"int or float; not a {arg.__class__.__name__}."
                )
        self.s1 = s1
        self.s2 = s2

        if not isinstance(v, Scalar):
            raise TypeError(
                f"v must be a Scalar not a {v.__class__.__name__}"
            )

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.s1 is other.s1 and self.s2 is other.s2 and self.v is other.v

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}<{self.v} = {self.s1} {self._operator_character} {self.s2}>"


class ScalarAssociativeBinaryConstraint(ScalarBinaryConstraint, ABC):

    def __eq__(self, other: Any) -> bool:
        if super().__eq__(other):
            return True

        if not isinstance(other, self.__class__):
            return False
        if self.s1 is other.s2 and self.s2 is other.s1 and self.v is other.v:
            return True

        return False


class AdditiveConstraint(ScalarAssociativeBinaryConstraint):
    """Constrains a Scalar to the sum of two other Scalars."""

    _operator_character = '+'

    def error(self) -> float:
        return lambda x: abs(self._s1.value + self._s2.value - x)


class SubtractiveConstraint(ScalarBinaryConstraint):
    """Constrains a Scalar to the difference of two other Scalars."""

    _operator_character = '-'


class MultiplicativeConstraint(ScalarAssociativeBinaryConstraint):
    """Constrains a Scalar to the multiple of two other Scalars."""

    _operator_character = '*'


class DivisiveConstraint(ScalarBinaryConstraint):
    """Constrains a Scalar to the ratio of two other Scalars."""

    _operator_character = '/'
