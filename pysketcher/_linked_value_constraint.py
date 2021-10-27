from __future__ import annotations

from ._constrainable import Constrainable
from ._value_constraint import ValueConstraint


class LinkedValueConstraint(ValueConstraint[Constrainable]):
    """Used to indicate that a ConstraintSet is constrained to a value of another."""

    def __init__(self, constraint_set) -> None:
        if not isinstance(constraint_set, Constrainable):
            raise TypeError(
                "LinkedValueConstraint must be initialized with a Constrainable subclass.")
        super().__init__(constraint_set)

    def apply_reciprocal_constraint(self, instance: Constrainable) -> None:
        self.constraint_set.constrain_with(LinkedValueConstraint(instance))

    def cascade_constraints(self, instance) -> None:
        pass

    @property
    def constraint_set(self):
        return self.value
