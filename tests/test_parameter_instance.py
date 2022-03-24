from pysketcher import (
    Constraint,
    ParameterInstance,
)


class TestParameterInstance:
    class MockConstraint(Constraint):
        ...

    def test_constrain_with(self):
        under_test = ParameterInstance()
        constraint = self.MockConstraint()
        under_test.constrain_with(constraint)
        assert under_test.constraints == [constraint]

    def test_reset_constraints(self):
        under_test = ParameterInstance()
        constraint = self.MockConstraint()
        under_test.constrain_with(constraint)
        under_test.reset_constraints()
        assert under_test.constraints == []

    def test_repr(self):
        under_test = ParameterInstance()
        assert repr(under_test) == "ParameterInstance()"

        under_test = ParameterInstance(name="test")
        assert repr(under_test) == "test: ParameterInstance()"

        # TODO: test display of constraints

    def test_str(self):
        under_test = ParameterInstance(name="test")
        assert under_test.__str__() == "test"
        assert str(under_test) == "test"
