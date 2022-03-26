from .contract_scalar_binary_constraint import ContractScalarBinaryConstraint

from pysketcher import AdditiveConstraint


class TestAdditiveConstraint(ContractScalarBinaryConstraint[AdditiveConstraint]):
    _class = AdditiveConstraint
