# Stubs for torch.nn.modules.adaptive (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..functional import log_softmax
from .module import Module
from collections import namedtuple
from typing import Any

_ASMoutput = namedtuple('ASMoutput', ['output', 'loss'])

class AdaptiveLogSoftmaxWithLoss(Module):
    in_features: Any = ...
    n_classes: Any = ...
    cutoffs: Any = ...
    div_value: Any = ...
    head_bias: Any = ...
    shortlist_size: Any = ...
    n_clusters: Any = ...
    head_size: Any = ...
    head: Any = ...
    tail: Any = ...
    def __init__(self, in_features: Any, n_classes: Any, cutoffs: Any, div_value: float = ..., head_bias: bool = ...) -> None: ...
    def reset_parameters(self) -> None: ...
    def forward(self, input: Any, target: Any): ...
    def log_prob(self, input: Any): ...
    def predict(self, input: Any): ...