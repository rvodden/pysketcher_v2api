from typing import List

from ._constraint import Constraint
from ._resolvable import Resolvable


class ConstraintSet(Resolvable):
    def __init__(self, name=""):
        self._constraints: List[Constraint] = []
        self._name: str = name

    def constrain_with(self, constraint: Constraint) -> None:
        constraint.validate_object(self)
        if constraint in self._constraints:
            return
        """Add a constraint to this objects list of constraints."""
        self._constraints.append(constraint)
        constraint.cascade_constraints(self)
        constraint.apply_reciprocal_constraint(self)

    def reset_constraints(self) -> None:
        """Removes the existing constraints from the constraint set."""
        self._constraints = []

    def __repr__(self) -> str:
        retval = f"{self._name}: " if self._name != "" else ""
        retval += f"{self.__class__.__name__}("
        if len(self._constraints) == 0:
            retval += ")"
            return retval

        for constraint in self._constraints:
            retval += f"\n    {constraint}"
        retval += "\n)"
        return retval

    def __str__(self) -> str:
        return self._name

    @property
    def constraints(self) -> List[Constraint]:
        return self._constraints
