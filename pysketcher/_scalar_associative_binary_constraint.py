from ._scalar_binary_constraint import ScalarBinaryConstraint

class ScalarAssociativeBinaryConstraint(ScalarBinaryConstraint):
    def __eq__(self, other) -> bool:
        if super().__eq__(other):
            return True
        if not isinstance(other, self.__class__):
            return False
        return self._s2 is other._s1 and self._s1 is other._s2

        
