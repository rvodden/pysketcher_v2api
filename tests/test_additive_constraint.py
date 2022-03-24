from contract_scalar_associative_binary_constraint import ContractScalarAssociativeBinaryConstraint

from pysketcher import AdditiveConstraint, Scalar, SubtractiveConstraint


class TestAdditiveConstraint(ContractScalarAssociativeBinaryConstraint[AdditiveConstraint]):
    _class = AdditiveConstraint

    # def test_recipriocal_cosntraint(self):
    #     s1 = Scalar()
    #     s2 = Scalar()

    #     s3 = Scalar()
    #     s3.constrain_with(AdditiveConstraint(s1, s2))

    #     assert SubtractiveConstraint(s3, s1) in s2.constraints
    #     assert SubtractiveConstraint(s3, s2) in s1.constraints
