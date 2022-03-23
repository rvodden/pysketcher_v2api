from abc import ABC
from typing import TypeVar
from pysketcher import Scalar

from contract_scalar_binary_constraint import ContractScalarBinaryConstraint

T = TypeVar("T")
class ContractScalarAssociativeBinaryConstraint(ContractScalarBinaryConstraint[T], ABC):

    def test_associative_equality(self):
        s1 = Scalar()
        s2 = Scalar()

        ut1 = self.make_one(s1, s2)
        ut2 = self.make_one(s2, s1)

        assert ut1 == ut2