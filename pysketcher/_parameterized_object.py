from __future__ import annotations


class ParameterizedObject:
    _parameter_instances: list[str]
    _name: str

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def parameters(self) -> list[ParameterInstance]:
        retval = []
        for parameter_instance in self._parameter_instances:
            retval.append(getattr(self, parameter_instance))
        return retval


from ._parameter_instance import ParameterInstance  # noqa: E402
