from abc import ABC
from typing import Type, TypeVar

from contract_scalar_constraint import ContractScalarConstraint

from pysketcher import Scalar


T = TypeVar("T")


class ContractScalarBinaryConstraint(ContractScalarConstraint[T], ABC):
    _class: Type[T]

    def make_one(self, s1=None, s2=None):
        if not s1:
            s1 = Scalar()
        if not s2:
            s2 = Scalar()
        return self._class(s1, s2)

    def test_equality(self):
        s1 = Scalar()
        s2 = Scalar()

        ut1 = self.make_one(s1, s2)
        ut2 = self.make_one(s1, s2)

        assert ut1 == ut2

    def test_inequality(self):
        s1 = Scalar()
        s2 = Scalar()
        s3 = Scalar()

        ut1 = self.make_one(s1, s2)
        ut2 = self.make_one(s1, s3)

        assert ut1 != ut2
        assert ut1 != "Invalid Type"

    def test_repr(self):
        s1 = Scalar()
        s2 = Scalar()
        under_test = self.make_one(s1, s2)

        assert repr(under_test) == f"{self._class.__name__}<{s1}, {s2}>"
