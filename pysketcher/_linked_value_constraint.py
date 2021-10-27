from ._constraint import Constraint
from ._constraint_set import ConstraintSet
from ._value_constraint import ValueConstraint


class LinkedValueConstraint(ValueConstraint[Constraint]):
    """Used to indicate that a ConstraintSet is constrained to a value of another."""

    def __init__(self, constraint_set) -> None:
        if not isinstance(constraint_set, ConstraintSet):
            raise TypeError(
                "LinkedValueConstraint must be initialized with a ConstraintSet subclass.")
        super().__init__(constraint_set)

    def apply_reciprocal_constraint(self, instance: Constraint) -> None:
        self.constraint_set.constrain_with(LinkedValueConstraint(instance))

    def cascade_constraints(self, instance) -> None:
        pass

    @property
    def constraint_set(self):
        return self.value

