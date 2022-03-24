class Parameter:
    """An object which can be passed around to represent a value."""

    def __init__(self, parameter_instance_type) -> None:
        self._parameter_instance_type = parameter_instance_type

    def __set_name__(self, owner, name) -> None:
        self.public_name = name
        self.private_name = f"_{name}"
        # append the name to the list of ConstrainedSets on the class
        # creating that list if it doesn't exist
        try:
            parameter_instances = owner._parameter_instances
        except AttributeError:
            parameter_instances = []
            owner._parameter_instances = parameter_instances
        finally:
            owner._parameter_instances.append(self.public_name)

    def __get__(self, parameterized_object, typ=None):
        # grab the ParameterInstance from the ParameterizedObject
        try:
            parameter_instance = getattr(parameterized_object, self.private_name)
        except AttributeError:
            # If the instance didn't have an initialized ParameterInstance then
            # give it one
            parameter_instance = self._parameter_instance_type(
                name=f"{parameterized_object.name}.{self.public_name}"
            )
            setattr(parameterized_object, self.private_name, parameter_instance)
        return parameter_instance

    def __set__(self, instance, value) -> None:
        # Grab the ConstraintSet from the instance
        parameter_instance: ParameterInstance = self.__get__(instance, None)

        # if the value we've been asked to assign is a ConstraintSet
        if isinstance(value, ParameterInstance):
            # then overwrite the existing constraint set with this one:
            setattr(instance, self.private_name, value)

        # resolve the value of the ParameterInstance:
        parameter_instance.set(value, resolve=True)


from ._parameter_instance import ParameterInstance  # noqa: E402, I100, I101, I202
