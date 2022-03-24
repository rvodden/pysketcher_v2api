from __future__ import annotations

from abc import abstractmethod, ABC


class Constraint(ABC):
    """Used to restrict the value of a `ConstrainedValue`."""

    def __init__(self):
        self._value = None
        self._resolved = False

    def validate_object(self, instance: ParameterInstance) -> None:
        """Checks `instance` is suitable. Raises `InvalidConstraintException` if not."""

    def apply_reciprocal_constraint(self, instance: ParameterInstance) -> None:
        """Applies a matching constraint to the provided instance."""

    def cascade_constraints(self, instance: ParameterInstance) -> None:
        """Applies appropriate constraints to the properties of `instance`."""

from ._parameter_instance import ParameterInstance
