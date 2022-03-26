from .contract_scalar_binary_constraint import ContractScalarBinaryConstraint

from pysketcher import MultiplicativeConstraint


class TestMultiplicativeConstraint(
    ContractScalarBinaryConstraint[MultiplicativeConstraint]
):
    _class = MultiplicativeConstraint
