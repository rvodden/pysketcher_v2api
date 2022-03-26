from abc import ABC
from typing import Type, TypeVar

from .contract_scalar_constraint import ContractScalarConstraint
from pysketcher import Scalar


T = TypeVar("T")


class ContractScalarBinaryConstraint(ContractScalarConstraint[T], ABC):
    _class: Type[T]

    def make_one(self, name="test", v=None, s1=None, s2=None):
        if not v:
            v = Scalar("v")
        if not s1:
            s1 = Scalar("s1")
        if not s2:
            s2 = Scalar("s2")
        return self._class(name, v, s1, s2)

    def test_equality(self):
        v = Scalar("v")
        s1 = Scalar("s1")
        s2 = Scalar("s2")

        ut1 = self.make_one("ut1", v, s1, s2)
        ut2 = self.make_one("ut2", v, s1, s2)

        assert ut1 == ut2

    def test_inequality(self):
        v = Scalar("v")
        s1 = Scalar("s1")
        s2 = Scalar("s2")
        s3 = Scalar("s3")

        ut1 = self.make_one("ut1", v, s1, s2)
        ut2 = self.make_one("ut2", v, s1, s3)

        assert ut1 != ut2
        assert ut1 != "Invalid Type"

    def test_repr(self):
        v = Scalar("v")
        s1 = Scalar("s1")
        s2 = Scalar("s2")
        under_test = self.make_one("under_test", v, s1, s2)

        assert repr(under_test) == f"{self._class.__name__}<{v} = {s1} {under_test._operator_character} {s2}>"
