from ._constraint_set import ConstraintSet
from ._fixed_value_constraint import FixedValueConstraint
from ._linked_value_constraint import LinkedValueConstraint


class ConstrainedValue:
    """An object which can be passed around to represent a value."""

    def __init__(self, constraint_set_class) -> None:
        self._constraint_set_class = constraint_set_class

    def __set_name__(self, owner, name) -> None:
        self.public_name = name
        self.private_name = f"_{name}"
        # append the name to the list of ConstrainedSets on the class
        # creating that list if it doesn't exist
        try:
            constraint_sets = owner._constraint_sets
        except AttributeError:
            constraint_sets = []
            owner._constraint_sets = constraint_sets
        finally:
            owner._constraint_sets.append(self.public_name)

    def __get__(self, instance, typ=None):
        # grab the ConstraintSet from the instance
        try:
            constraint_set = getattr(instance, self.private_name)
        except AttributeError:
            # If the instance didn't have an initialized ConstraintSet then
            # give it one
            constraint_set = self._constraint_set_class(
                name=f"{instance.name}.{self.public_name}"
            )
            setattr(instance, self.private_name, constraint_set)
        return constraint_set

    def __set__(self, instance, value) -> None:
        # Grab the ConstraintSet from the instance
        constraint_set: ConstraintSet = self.__get__(instance, None)

        # if the value we've been asked to assign is a ConstraintSet
        # then add a LinkedValueConstraint:
        if isinstance(value, ConstraintSet):
            constraint_set.constrain_with(LinkedValueConstraint(value))
            return

        # otherwise use a FixedValueConstraint to constrain to the provided
        # value
        constraint_set.constrain_with(FixedValueConstraint(value))
