# Stubs for torch.distributions.constraint_registry (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class ConstraintRegistry:
    def __init__(self) -> None: ...
    def register(self, constraint: Any, factory: Optional[Any] = ...): ...
    def __call__(self, constraint: Any): ...

biject_to: Any
transform_to: Any
