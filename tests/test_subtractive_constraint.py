from contract_scalar_binary_constraint import ContractScalarBinaryConstraint

from pysketcher import SubtractiveConstraint


class TestSubtractiveConstraint(ContractScalarBinaryConstraint[SubtractiveConstraint]):
    _class = SubtractiveConstraint
