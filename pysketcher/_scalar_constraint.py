from abc import ABC
from typing import Any

from ._abstract_scalar import AbstractScalar
from ._constraint import Constraint
from ._error import InvalidConstraintException


class ScalarConstraint(Constraint, ABC):
    """A constraint which applies to a Scalar."""

    def validate_object(self, instance) -> None:
        if not self._is_scalar(instance):
            return InvalidConstraintException(
                f"{self.__class__.__name__} can only be applied to"
                f"Scalar, it cannot be applied to  {instance.__class__.__name__}."
            )

    @staticmethod
    def _is_scalar(obj: Any):
        return isinstance(obj, AbstractScalar)
