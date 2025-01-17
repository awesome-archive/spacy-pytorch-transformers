# Stubs for torch.nn.modules.pooling (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..._jit_internal import weak_module, weak_script_method
from .module import Module
from .utils import _pair, _single, _triple
from typing import Any, Optional

class _MaxPoolNd(Module):
    __constants__: Any = ...
    kernel_size: Any = ...
    stride: Any = ...
    padding: Any = ...
    dilation: Any = ...
    return_indices: Any = ...
    ceil_mode: Any = ...
    def __init__(self, kernel_size: Any, stride: Optional[Any] = ..., padding: int = ..., dilation: int = ..., return_indices: bool = ..., ceil_mode: bool = ...) -> None: ...
    def extra_repr(self): ...

class MaxPool1d(_MaxPoolNd):
    def forward(self, input: Any): ...
    def extra_repr(self): ...

class MaxPool2d(_MaxPoolNd):
    def forward(self, input: Any): ...

class MaxPool3d(_MaxPoolNd):
    def forward(self, input: Any): ...

class _MaxUnpoolNd(Module):
    def extra_repr(self): ...

class MaxUnpool1d(_MaxUnpoolNd):
    kernel_size: Any = ...
    stride: Any = ...
    padding: Any = ...
    def __init__(self, kernel_size: Any, stride: Optional[Any] = ..., padding: int = ...) -> None: ...
    def forward(self, input: Any, indices: Any, output_size: Optional[Any] = ...): ...

class MaxUnpool2d(_MaxUnpoolNd):
    kernel_size: Any = ...
    stride: Any = ...
    padding: Any = ...
    def __init__(self, kernel_size: Any, stride: Optional[Any] = ..., padding: int = ...) -> None: ...
    def forward(self, input: Any, indices: Any, output_size: Optional[Any] = ...): ...

class MaxUnpool3d(_MaxUnpoolNd):
    kernel_size: Any = ...
    stride: Any = ...
    padding: Any = ...
    def __init__(self, kernel_size: Any, stride: Optional[Any] = ..., padding: int = ...) -> None: ...
    def forward(self, input: Any, indices: Any, output_size: Optional[Any] = ...): ...

class _AvgPoolNd(Module):
    __constants__: Any = ...
    def extra_repr(self): ...

class AvgPool1d(_AvgPoolNd):
    kernel_size: Any = ...
    stride: Any = ...
    padding: Any = ...
    ceil_mode: Any = ...
    count_include_pad: Any = ...
    def __init__(self, kernel_size: Any, stride: Optional[Any] = ..., padding: int = ..., ceil_mode: bool = ..., count_include_pad: bool = ...) -> None: ...
    def forward(self, input: Any): ...

class AvgPool2d(_AvgPoolNd):
    kernel_size: Any = ...
    stride: Any = ...
    padding: Any = ...
    ceil_mode: Any = ...
    count_include_pad: Any = ...
    def __init__(self, kernel_size: Any, stride: Optional[Any] = ..., padding: int = ..., ceil_mode: bool = ..., count_include_pad: bool = ...) -> None: ...
    def forward(self, input: Any): ...

class AvgPool3d(_AvgPoolNd):
    kernel_size: Any = ...
    stride: Any = ...
    padding: Any = ...
    ceil_mode: Any = ...
    count_include_pad: Any = ...
    def __init__(self, kernel_size: Any, stride: Optional[Any] = ..., padding: int = ..., ceil_mode: bool = ..., count_include_pad: bool = ...) -> None: ...
    def forward(self, input: Any): ...

class FractionalMaxPool2d(Module):
    __constants__: Any = ...
    kernel_size: Any = ...
    return_indices: Any = ...
    output_size: Any = ...
    output_ratio: Any = ...
    def __init__(self, kernel_size: Any, output_size: Optional[Any] = ..., output_ratio: Optional[Any] = ..., return_indices: bool = ..., _random_samples: Optional[Any] = ...) -> None: ...
    def forward(self, input: Any): ...

class FractionalMaxPool3d(Module):
    __constants__: Any = ...
    kernel_size: Any = ...
    return_indices: Any = ...
    output_size: Any = ...
    output_ratio: Any = ...
    def __init__(self, kernel_size: Any, output_size: Optional[Any] = ..., output_ratio: Optional[Any] = ..., return_indices: bool = ..., _random_samples: Optional[Any] = ...) -> None: ...
    def forward(self, input: Any): ...

class _LPPoolNd(Module):
    __constants__: Any = ...
    norm_type: Any = ...
    kernel_size: Any = ...
    stride: Any = ...
    ceil_mode: Any = ...
    def __init__(self, norm_type: Any, kernel_size: Any, stride: Optional[Any] = ..., ceil_mode: bool = ...) -> None: ...
    def extra_repr(self): ...

class LPPool1d(_LPPoolNd):
    def forward(self, input: Any): ...

class LPPool2d(_LPPoolNd):
    def forward(self, input: Any): ...

class _AdaptiveMaxPoolNd(Module):
    __constants__: Any = ...
    output_size: Any = ...
    return_indices: Any = ...
    def __init__(self, output_size: Any, return_indices: bool = ...) -> None: ...
    def extra_repr(self): ...

class AdaptiveMaxPool1d(_AdaptiveMaxPoolNd):
    def forward(self, input: Any): ...

class AdaptiveMaxPool2d(_AdaptiveMaxPoolNd):
    def forward(self, input: Any): ...

class AdaptiveMaxPool3d(_AdaptiveMaxPoolNd):
    def forward(self, input: Any): ...

class _AdaptiveAvgPoolNd(Module):
    __constants__: Any = ...
    output_size: Any = ...
    def __init__(self, output_size: Any) -> None: ...
    def extra_repr(self): ...

class AdaptiveAvgPool1d(_AdaptiveAvgPoolNd):
    def forward(self, input: Any): ...

class AdaptiveAvgPool2d(_AdaptiveAvgPoolNd):
    def forward(self, input: Any): ...

class AdaptiveAvgPool3d(_AdaptiveAvgPoolNd):
    def forward(self, input: Any): ...
