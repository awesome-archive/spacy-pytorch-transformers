# Stubs for torch.distributions.log_normal (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from torch.distributions.transformed_distribution import TransformedDistribution
from typing import Any, Optional

class LogNormal(TransformedDistribution):
    arg_constraints: Any = ...
    support: Any = ...
    has_rsample: bool = ...
    def __init__(self, loc: Any, scale: Any, validate_args: Optional[Any] = ...) -> None: ...
    def expand(self, batch_shape: Any, _instance: Optional[Any] = ...): ...
    @property
    def loc(self): ...
    @property
    def scale(self): ...
    @property
    def mean(self): ...
    @property
    def variance(self): ...
    def entropy(self): ...
