from __future__ import annotations

from abc import ABC


class Constraint(ABC):
    """Used to restrict the value of a `ConstrainedValue`."""

    def validate_object(self, instance: Constraint) -> None:
        """Checks `instance` is suitable. Raises `InvalidConstraintException` if not."""

    def apply_reciprocal_constraint(self, instance: Constraint) -> None:
        """Applies a matching constraint to the provided instance."""

    def cascade_constraints(self, instance: Constraint) -> None:
        """Applies appropriate constraints to the properties of `instance`."""
