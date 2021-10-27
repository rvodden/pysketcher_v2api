from __future__ import annotations
from typing import Protocol, runtime_checkable


@runtime_checkable
class Constraint(Protocol):
    """Used to restrict the value of a `ConstrainedValue`."""

    def validate_object(self, instance: Constrainable) -> None:
        """Validates that `instance` is suitable. Raises `InvalidConstraintException` if not."""

    def apply_reciprocal_constraint(self, instance: Constrainable) -> None:
        """Applies a matching constraint to the provided instance."""

    def cascade_constraints(self, instance: Constrainable) -> None:
        """Applies appropriate constraints to the properties of `instance`."""
