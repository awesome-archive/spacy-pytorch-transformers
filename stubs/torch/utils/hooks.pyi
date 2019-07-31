# Stubs for torch.utils.hooks (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class RemovableHandle:
    next_id: int = ...
    hooks_dict_ref: Any = ...
    id: Any = ...
    def __init__(self, hooks_dict: Any) -> None: ...
    def remove(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type: Any, value: Any, tb: Any) -> None: ...

def unserializable_hook(f: Any): ...
def warn_if_has_hooks(tensor: Any) -> None: ...