from ._parameter_instance import ParameterInstance


class ConstrainedObject:
    _constraint_sets: list[str]
    _name: str

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def parameters(self) -> list[ParameterInstance]:
        retval = []
        for cs in self._constraint_sets:
            retval.append(getattr(self, cs))
        return retval
