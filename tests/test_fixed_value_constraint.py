from __future__ import annotations

import pytest

from pysketcher import ConstraintSet, FixedValueConstraint, InvalidConstraintException


class TestFixedValueConstraint:
    def test_value(self):
        constraint = FixedValueConstraint(3)
        assert constraint.value == 3

    def test_repr(self):
        value = "123"
        constraint1 = FixedValueConstraint(value)
        assert repr(constraint1) == f"FixedValueConstraint<{value}>"

    def test_validate_object(self):
        constraint = FixedValueConstraint(3)
        with pytest.raises(InvalidConstraintException):
            constraint.validate_object(3)

        cs = ConstraintSet(name="test")
        try:
            constraint.validate_object(cs)
        except InvalidConstraintException as e:
            raise AssertionError from e

        assert True

    def test_equality(self):
        constraint1 = FixedValueConstraint(1)
        constraint2 = FixedValueConstraint(1)
        assert constraint1 == constraint2
