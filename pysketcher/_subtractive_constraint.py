from ._scalar_binary_constraint import ScalarBinaryConstraint


class SubtractiveConstraint(ScalarBinaryConstraint):
    """Constrains a Scalar to the difference of two other Scalars."""

    def apply_reciprocal_constraint(self, instance) -> None:
        # instance = s1 - s2
        # s1 = instance + s2
        # s2 = s1 - instance
        if self._is_scalar(self._s1):
            self._s1.constrain_with(AdditiveConstraint(instance, self._s2))
        if self._is_scalar(self._s2):
            self._s2.constrain_with(SubtractiveConstraint(self._s1, instance))


from ._additive_constraint import AdditiveConstraint  # noqa: E402, I100, I101, I202
