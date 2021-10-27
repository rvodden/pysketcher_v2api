class UnderConstrainedError(RuntimeError):
    """Insufficient constraints have been provided to calculate a value."""

    pass


class InvalidConstraintException(TypeError):
    """A constraint has been applied to an object which doesn't make sense."""

    pass
