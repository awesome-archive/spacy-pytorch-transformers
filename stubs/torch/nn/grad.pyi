# Stubs for torch.nn.grad (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .modules.utils import _pair, _single, _triple
from typing import Any

def conv1d_input(input_size: Any, weight: Any, grad_output: Any, stride: int = ..., padding: int = ..., dilation: int = ..., groups: int = ...): ...
def conv1d_weight(input: Any, weight_size: Any, grad_output: Any, stride: int = ..., padding: int = ..., dilation: int = ..., groups: int = ...): ...
def conv2d_input(input_size: Any, weight: Any, grad_output: Any, stride: int = ..., padding: int = ..., dilation: int = ..., groups: int = ...): ...
def conv2d_weight(input: Any, weight_size: Any, grad_output: Any, stride: int = ..., padding: int = ..., dilation: int = ..., groups: int = ...): ...
def conv3d_input(input_size: Any, weight: Any, grad_output: Any, stride: int = ..., padding: int = ..., dilation: int = ..., groups: int = ...): ...
def conv3d_weight(input: Any, weight_size: Any, grad_output: Any, stride: int = ..., padding: int = ..., dilation: int = ..., groups: int = ...): ...
