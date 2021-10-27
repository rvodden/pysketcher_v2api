class UnderConstrainedError(RuntimeError):
    """Indicates that insufficient constraints have been provided to calculate a value."""
    pass


class InvalidConstraintException(TypeError):
    """Indicates that a constraint has been applied to an object which doesn't make sense."""

    pass
