import pytest

from pysketcher import ConstraintSet, InvalidConstraintException, LinkedValueConstraint


class TestLinkedValueConstraint:
    def test_initializer(self):
        with pytest.raises(TypeError):
            under_test = LinkedValueConstraint("Invalid Type")

        cs = ConstraintSet(name="link")
        under_test = LinkedValueConstraint(cs)
        assert under_test.value == cs

    def test_value(self):
        constraint_set = ConstraintSet()
        constraint = LinkedValueConstraint(constraint_set)
        assert constraint.value == constraint_set

    def test_repr(self):
        constraint_set = ConstraintSet()
        constraint1 = LinkedValueConstraint(constraint_set)
        assert repr(constraint1) == f"LinkedValueConstraint<{constraint_set}>"

    def test_validate_object(self):
        constraint_set = ConstraintSet()
        constraint = LinkedValueConstraint(constraint_set)
        with pytest.raises(InvalidConstraintException):
            constraint.validate_object(3)

        cs = ConstraintSet(name="test")
        try:
            constraint.validate_object(cs)
        except InvalidConstraintException as e:
            raise AssertionError from e

        assert True

    def test_equality(self):
        cs = ConstraintSet()
        constraint1 = LinkedValueConstraint(cs)
        constraint2 = LinkedValueConstraint(cs)
        assert constraint1 == constraint2
