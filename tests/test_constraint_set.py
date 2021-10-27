from pysketcher import Constraint, ConstraintSet, FixedValueConstraint


class TestConstraintSet:
    class MockConstraint(Constraint):
        ...
    
    def test_constrain_with(self):
        under_test = ConstraintSet()
        constraint = self.MockConstraint()
        under_test.constrain_with(constraint)
        assert under_test.constraints == [constraint]

    def test_reset_constraints(self):
        under_test = ConstraintSet()
        constraint = self.MockConstraint()
        under_test.constrain_with(constraint)
        under_test.reset_constraints()
        assert under_test.constraints == []

    def test_repr(self):
        under_test = ConstraintSet()
        assert repr(under_test) == "ConstraintSet()"

        under_test = ConstraintSet(name="test")
        assert repr(under_test) == "test: ConstraintSet()"

        constraint = FixedValueConstraint(5)
        under_test.constrain_with(constraint)
        assert (
            repr(under_test) == f"test: ConstraintSet(\n    {constraint}\n)"
        )

    def test_str(self):
        under_test = ConstraintSet(name="test")
        assert under_test.__str__() == "test"
        assert str(under_test) == "test"