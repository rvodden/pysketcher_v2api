from contract_scalar_associative_binary_constraint import ContractScalarAssociativeBinaryConstraint

from pysketcher import Scalar, MultiplicativeConstraint, DivisiveConstraint


class TestMultiplicativeConstraint(
    ContractScalarAssociativeBinaryConstraint[MultiplicativeConstraint]
):
    _class = MultiplicativeConstraint

    def test_recipriocal_cosntraint(self):
        s1 = Scalar()
        s2 = Scalar()

        s3 = Scalar()
        s3.constrain_with(MultiplicativeConstraint(s1, s2))

        assert DivisiveConstraint(s3, s2) in s1.constraints
        assert DivisiveConstraint(s3, s1) in s2.constraints
