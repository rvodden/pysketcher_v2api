from __future__ import annotations
from typing import Protocol, runtime_checkable

@runtime_checkable
class Constrainable(Protocol):
    def constrain_with(self, constraint: Constraint) -> None:
        pass
    
    def reset_constraints(self) -> None:
        pass