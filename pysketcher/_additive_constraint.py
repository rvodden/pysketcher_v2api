from ._scalar_associative_binary_constraint import ScalarAssociativeBinaryConstraint


class AdditiveConstraint(ScalarAssociativeBinaryConstraint):
    """Constrains a Scalar to the sum of two other Scalars."""

    def apply_reciprocal_constraint(self, instance) -> None:
        # instance = s1 + s2
        # s1 = instance - s2
        # s2 = instance - s1
        if self._is_scalar(self._s1):
            self._s1.constrain_with(SubtractiveConstraint(instance, self._s2))
        if self._is_scalar(self._s2):
            self._s2.constrain_with(SubtractiveConstraint(instance, self._s1))

    def error(self) -> float:
        return lambda x: abs(self._s1.value + self._s2.value - x) 

from ._subtractive_constraint import (  # noqa: B950, E402, I100, I101, I202
    SubtractiveConstraint,
)
from ._parameter_instance import ParameterInstance
