from pysketcher import Scalar


class TestScalar:
    def test_adding_two_scalars(self):
        s1 = Scalar()
        s2 = Scalar()

        s3 = s1 + s2
        assert isinstance(s3, Scalar)
        s3 = 3 + s2
        assert isinstance(s3, Scalar)
        s3 = s1 + 3
        assert isinstance(s3, Scalar)
        s3 = 3.5 + s2
        assert isinstance(s3, Scalar)
        s3 = s1 + 3.5
        assert isinstance(s3, Scalar)

    def test_subtracting_two_scalars(self):
        s1 = Scalar()
        s2 = Scalar()

        s3 = s1 - s2
        assert isinstance(s3, Scalar)

    def test_multiplying_two_scalars(self):
        s1 = Scalar()
        s2 = Scalar()

        s3 = s1 * s2
        assert isinstance(s3, Scalar)
        s3 = s1 * 2
        assert isinstance(s3, Scalar)
        s3 = 2 * s2
        assert isinstance(s3, Scalar)
        s3 = s1 * 2.5
        assert isinstance(s3, Scalar)
        s3 = 2.5 * s2
        assert isinstance(s3, Scalar)

    def test_dividing_two_scalars(self):
        s1 = Scalar()
        s2 = Scalar()

        s3 = s1 / s2
        assert isinstance(s3, Scalar)
