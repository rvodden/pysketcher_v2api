from contract_scalar_binary_constraint import ContractScalarBinaryConstraint

from pysketcher import DivisiveConstraint, MultiplicativeConstraint, Scalar


class TestDivisiveConstraint(ContractScalarBinaryConstraint[DivisiveConstraint]):
    _class = DivisiveConstraint

    # def test_recipriocal_cosntraint(self):
    #     s1 = Scalar()
    #     s2 = Scalar()

    #     s3 = Scalar()
    #     s3.constrain_with(DivisiveConstraint(s1, s2))

    #     assert MultiplicativeConstraint(s2, s3) in s1.constraints
    #     assert DivisiveConstraint(s1, s3) in s2.constraints