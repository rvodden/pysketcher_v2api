from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from ._constraint import Constraint  # noqa: E402, I100, I101, I202
from ._constraint_set import ConstraintSet
from ._error import InvalidConstraintException


T = TypeVar("T")


class ValueConstraint(Constraint, Generic[T], ABC):
    """A base class which allows a constraint to take a value."""

    def __init__(self, value: T) -> None:
        self._value: T = value
        super().__init__()

    @property
    def value(self) -> T:
        return self._value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}<{self.value}>"

    def validate_object(self, instance) -> None:
        if not isinstance(instance, ConstraintSet):
            raise InvalidConstraintException(
                f"{self.__class__.__name__} can only"
                f" be applied to `ConstraintSet`, it"
                f" cannot be applied to `{instance.__class__.__name__}`"
            )

    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__) and self.value == other.value

    def apply_reciprocal_constraint(self, instance: Constraint) -> None:
        pass

    def cascade_constraints(self, instance: Constraint) -> None:
        pass
