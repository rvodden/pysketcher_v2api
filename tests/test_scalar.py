from pysketcher import Scalar


class TestScalar:
    def test_adding_two_scalars(self):
        s1 = Scalar()
        s2 = Scalar()

        s3 = s1 + s2
        assert isinstance(s3, Scalar)
