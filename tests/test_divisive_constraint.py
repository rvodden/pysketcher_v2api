from .contract_scalar_binary_constraint import ContractScalarBinaryConstraint

from pysketcher import DivisiveConstraint


class TestDivisiveConstraint(ContractScalarBinaryConstraint[DivisiveConstraint]):
    _class = DivisiveConstraint
