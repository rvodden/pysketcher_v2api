from pysketcher import (
    ConstrainedValue,
    ConstraintSet,
    FixedValueConstraint,
    LinkedValueConstraint,
)


class TestConstrainedValue:
    def test_set_name(self):
        class Mock:
            pass

        under_test = ConstrainedValue(ConstraintSet)
        under_test.__set_name__(Mock, "test_name")

        assert isinstance(Mock._constraint_sets, list)
        assert "test_name" in Mock._constraint_sets
        assert under_test.private_name == "_test_name"
        assert under_test.public_name == "test_name"

    def test_set_value(self):
        class Mock:
            pass

        mock = Mock()
        mock.name = "test"

        mock._constraint_sets = ["test_name"]

        under_test = ConstrainedValue(ConstraintSet)
        under_test.private_name = "_test_name"
        under_test.public_name = "test_name"

        under_test.__set__(mock, 5)

        assert isinstance(mock._test_name, ConstraintSet)
        constraint = mock._test_name._constraints[0]
        assert isinstance(constraint, FixedValueConstraint)
        assert constraint.value == 5

    def test_set_constraint_set(self):
        class Mock:
            pass

        mock = Mock()
        mock.name = "test"

        mock._constraint_sets = ["test_name"]

        under_test = ConstrainedValue(ConstraintSet)
        under_test.private_name = "_test_name"
        under_test.public_name = "test_name"

        constraint_set = ConstraintSet()

        under_test.__set__(mock, constraint_set)

        assert isinstance(mock._test_name, ConstraintSet)
        constraint = mock._test_name._constraints[0]
        assert isinstance(constraint, LinkedValueConstraint)
        assert constraint.value == constraint_set

    def test_get_value(self):
        class Mock:
            pass

        mock = Mock()
        mock.name = "test"

        mock._constraint_sets = ["test_name"]
        constraint_set = ConstraintSet(name="test_name")
        mock._test_name = constraint_set

        under_test = ConstrainedValue(ConstraintSet)
        under_test.private_name = "_test_name"
        under_test.public_name = "test_name"

        assert under_test.__get__(mock, Mock) is constraint_set

    def test_main_flow_value(self):
        class Mock:
            x = ConstrainedValue(ConstraintSet)

        mock = Mock()
        mock.name = "mock"
        mock.x = 5

        assert isinstance(mock.x, ConstraintSet)
        constraint = mock.x.constraints[0]
        assert isinstance(constraint, FixedValueConstraint)
        assert constraint.value == 5

    def test_main_flow_constraint_set(self):
        class Mock:
            x = ConstrainedValue(ConstraintSet)

        mock = Mock()
        mock.name = "mock"
        constraint_set = ConstraintSet()
        mock.x = constraint_set

        assert isinstance(mock.x, ConstraintSet)
        constraint = mock.x.constraints[0]
        assert isinstance(constraint, LinkedValueConstraint)
        assert constraint.value == constraint_set
