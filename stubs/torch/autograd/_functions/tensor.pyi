# Stubs for torch.autograd._functions.tensor (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..function import Function
from typing import Any

class Type(Function):
    @staticmethod
    def forward(ctx: Any, i: Any, dest_type: Any): ...
    @staticmethod
    def backward(ctx: Any, grad_output: Any): ...

class Resize(Function):
    @staticmethod
    def forward(ctx: Any, tensor: Any, sizes: Any): ...
    @staticmethod
    def backward(ctx: Any, grad_output: Any): ...
