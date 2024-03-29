import pytest

from pysketcher import AdditiveConstraint, DivisiveConstraint, MultiplicativeConstraint, Scalar, SubtractiveConstraint


_non_associative_examples: list[tuple] = [
    (Scalar("s1"), Scalar("s2")),
    (Scalar("s1"), 3),
    (Scalar("s1"), 3.5)
]

_examples: list[tuple] = _non_associative_examples + [
    (3, Scalar("s2")),
    (3.5, Scalar("s2"))
]

class TestScalar:
    @pytest.mark.parametrize("s1, s2", _examples)
    def test_addition(self, s1: Scalar, s2: Scalar):
        s3 = s1 + s2
        assert isinstance(s3, Scalar), "addition should created a new `Scalar`"
        assert AdditiveConstraint("add", s3, s1, s2) in s3.constraints, "addition should create an `AdditiveConstraint` in the new `Scalar`"

    def test_addition_with_invalid_type_raises_exception(self):
        with pytest.raises(TypeError):
            Scalar() + "incompatible type"

    @pytest.mark.parametrize("s1, s2", _non_associative_examples)
    def test_subtracting_two_scalars(self, s1, s2):
        s3 = s1 - s2
        assert isinstance(s3, Scalar)
        assert SubtractiveConstraint("sub", s3, s1, s2) in s3.constraints

    def test_subtraction_with_invalid_type_raises_exception(self):
        with pytest.raises(TypeError):
            Scalar() - "incompatible type"

    @pytest.mark.parametrize("s1, s2", _examples)
    def test_multiplication(self, s1, s2):
        s1 = Scalar("s1")
        s2 = Scalar("s2")

        s3 = s1 * s2
        assert isinstance(s3, Scalar)
        assert MultiplicativeConstraint("mul", s3, s1, s2) in s3.constraints

    def test_multiplication_with_invalid_type_raises_exception(self):
        with pytest.raises(TypeError):
            Scalar() * "incompatible type"

    @pytest.mark.parametrize("s1, s2", _non_associative_examples)
    def test_dividing_two_scalars(self, s1, s2):
        s1 = Scalar("s1")
        s2 = Scalar("s3")

        s3 = s1 / s2
        assert isinstance(s3, Scalar)
        assert DivisiveConstraint("div", s3, s1, s2) in s3.constraints

    def test_division_with_invalid_type_raises_exception(self):
        with pytest.raises(TypeError):
            Scalar() / "incompatible type"