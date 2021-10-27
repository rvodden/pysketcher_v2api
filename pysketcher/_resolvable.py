from abc import ABC
from typing import Any

from ._error import UnderConstrainedError


class Resolvable(ABC):
    """Temporary class to enabled testing of constraint networks."""
    def resolve(self) -> Any:
        """Naive implementation to aid testing"""
        for constraint in self._constraints:
            if type(constraint).__name__ == "FixedValueConstraint":
                return constraint.value
            if type(constraint).__name__ == "LinkedValueConstraint":
                return constraint.constraint_set.resolve()

        raise UnderConstrainedError("Fixed Value has not been provided.")
