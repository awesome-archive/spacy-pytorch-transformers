# Stubs for torch.nn.modules.conv (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..._jit_internal import List, weak_module, weak_script_method
from .module import Module
from .utils import _pair, _single, _triple
from typing import Any, Optional

class _ConvNd(Module):
    __constants__: Any = ...
    in_channels: Any = ...
    out_channels: Any = ...
    kernel_size: Any = ...
    stride: Any = ...
    padding: Any = ...
    dilation: Any = ...
    transposed: Any = ...
    output_padding: Any = ...
    groups: Any = ...
    padding_mode: Any = ...
    weight: Any = ...
    bias: Any = ...
    def __init__(self, in_channels: Any, out_channels: Any, kernel_size: Any, stride: Any, padding: Any, dilation: Any, transposed: Any, output_padding: Any, groups: Any, bias: Any, padding_mode: Any) -> None: ...
    def reset_parameters(self) -> None: ...
    def extra_repr(self): ...

class Conv1d(_ConvNd):
    def __init__(self, in_channels: Any, out_channels: Any, kernel_size: Any, stride: int = ..., padding: int = ..., dilation: int = ..., groups: int = ..., bias: bool = ..., padding_mode: str = ...) -> None: ...
    def forward(self, input: Any): ...

class Conv2d(_ConvNd):
    def __init__(self, in_channels: Any, out_channels: Any, kernel_size: Any, stride: int = ..., padding: int = ..., dilation: int = ..., groups: int = ..., bias: bool = ..., padding_mode: str = ...) -> None: ...
    def forward(self, input: Any): ...

class Conv3d(_ConvNd):
    def __init__(self, in_channels: Any, out_channels: Any, kernel_size: Any, stride: int = ..., padding: int = ..., dilation: int = ..., groups: int = ..., bias: bool = ..., padding_mode: str = ...) -> None: ...
    def forward(self, input: Any): ...

class _ConvTransposeMixin:
    __constants__: Any = ...
    def forward(self, input: Any, output_size: Optional[Any] = ...): ...

class ConvTranspose1d(_ConvTransposeMixin, _ConvNd):
    def __init__(self, in_channels: Any, out_channels: Any, kernel_size: Any, stride: int = ..., padding: int = ..., output_padding: int = ..., groups: int = ..., bias: bool = ..., dilation: int = ..., padding_mode: str = ...) -> None: ...
    def forward(self, input: Tensor, output_size: Optional[List[int]]=...) -> Tensor: ...

class ConvTranspose2d(_ConvTransposeMixin, _ConvNd):
    def __init__(self, in_channels: Any, out_channels: Any, kernel_size: Any, stride: int = ..., padding: int = ..., output_padding: int = ..., groups: int = ..., bias: bool = ..., dilation: int = ..., padding_mode: str = ...) -> None: ...
    def forward(self, input: Tensor, output_size: Optional[List[int]]=...) -> Tensor: ...

class ConvTranspose3d(_ConvTransposeMixin, _ConvNd):
    def __init__(self, in_channels: Any, out_channels: Any, kernel_size: Any, stride: int = ..., padding: int = ..., output_padding: int = ..., groups: int = ..., bias: bool = ..., dilation: int = ..., padding_mode: str = ...) -> None: ...
    def forward(self, input: Tensor, output_size: Optional[List[int]]=...) -> Tensor: ...
