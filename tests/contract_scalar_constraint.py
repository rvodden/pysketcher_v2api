from abc import ABC, abstractmethod
from typing import Generic, TypeVar

import pytest

from pysketcher import ParameterInstance, InvalidConstraintException, Scalar

T = TypeVar("T")


class ContractScalarConstraint(Generic[T], ABC):
    @abstractmethod
    def make_one(self):
        pass

    def test_validate_object_with_scalar(self):
        under_test = self.make_one()

        try:
            under_test.validate_object(Scalar())
        except InvalidConstraintException as e:
            raise AssertionError from e
        else:
            assert True

    def test_validate_object_with_non_scalar(self):
        under_test = self.make_one()

        cs = ParameterInstance(name="test")
        assert not under_test._is_scalar(cs)

        with pytest.raises(InvalidConstraintException):
            under_test.validate_object(ParameterInstance())
