from pysketcher import (
    Parameter,
    ParameterInstance,
)


class TestConstrainedValue:
    def test_set_name(self):
        class Mock:
            pass

        under_test = Parameter(ParameterInstance)
        under_test.__set_name__(Mock, "test_name")

        assert isinstance(Mock._parameter_instances, list)
        assert "test_name" in Mock._parameter_instances
        assert under_test.private_name == "_test_name"
        assert under_test.public_name == "test_name"

    def test_set_value(self):
        class Mock:
            pass

        mock = Mock()
        mock.name = "test"

        mock._parameter_instances = ["test_name"]

        under_test = Parameter(ParameterInstance)
        under_test.private_name = "_test_name"
        under_test.public_name = "test_name"

        under_test.__set__(mock, 5)

        assert isinstance(mock._test_name, ParameterInstance)
        assert mock._test_name._value == 5
        assert mock._test_name._resolved

    def test_set_parameter_instance(self):
        class Mock:
            pass

        mock = Mock()
        mock.name = "test"

        mock._parameter_instances = ["test_name"]

        under_test = Parameter(ParameterInstance)
        under_test.private_name = "_test_name"
        under_test.public_name = "test_name"

        parameter_instance = ParameterInstance()

        under_test.__set__(mock, parameter_instance)

        # assert isinstance(mock._test_name, ConstraintSet)
        # constraint = mock._test_name._constraints[0]
        # assert isinstance(constraint, LinkedValueConstraint)
        # assert constraint.value == parameter_instance

        assert under_test.__get__(mock) == parameter_instance

    def test_get_value(self):
        class Mock:
            pass

        mock = Mock()
        mock.name = "test"

        mock._parameter_instances = ["test_name"]
        parameter_instance = ParameterInstance(name="test_name")
        mock._test_name = parameter_instance

        under_test = Parameter(ParameterInstance)
        under_test.private_name = "_test_name"
        under_test.public_name = "test_name"

        assert under_test.__get__(mock, Mock) is parameter_instance

    def test_main_flow_value(self):
        class Mock:
            x = Parameter(ParameterInstance)

        mock = Mock()
        mock.name = "mock"
        mock.x = 5

        assert isinstance(mock.x, ParameterInstance)
        assert mock.x.value == 5
        assert mock.x._resolved == True

    def test_main_flow_parameter_instance(self):
        class Mock:
            x = Parameter(ParameterInstance)

        mock = Mock()
        mock.name = "mock"
        parameter_instance = ParameterInstance()
        mock.x = parameter_instance

        # assert isinstance(mock.x, ConstraintSet)
        # constraint = mock.x.constraints[0]
        # assert isinstance(constraint, LinkedValueConstraint)
        # assert constraint.value == parameter_instance
        assert mock.x == parameter_instance
