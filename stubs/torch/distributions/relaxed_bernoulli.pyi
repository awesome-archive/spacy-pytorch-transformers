# Stubs for torch.distributions.relaxed_bernoulli (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from torch.distributions.distribution import Distribution
from torch.distributions.transformed_distribution import TransformedDistribution
from typing import Any, Optional

class LogitRelaxedBernoulli(Distribution):
    arg_constraints: Any = ...
    support: Any = ...
    temperature: Any = ...
    def __init__(self, temperature: Any, probs: Optional[Any] = ..., logits: Optional[Any] = ..., validate_args: Optional[Any] = ...) -> None: ...
    def expand(self, batch_shape: Any, _instance: Optional[Any] = ...): ...
    def logits(self): ...
    def probs(self): ...
    @property
    def param_shape(self): ...
    def rsample(self, sample_shape: Any = ...): ...
    def log_prob(self, value: Any): ...

class RelaxedBernoulli(TransformedDistribution):
    arg_constraints: Any = ...
    support: Any = ...
    has_rsample: bool = ...
    def __init__(self, temperature: Any, probs: Optional[Any] = ..., logits: Optional[Any] = ..., validate_args: Optional[Any] = ...) -> None: ...
    def expand(self, batch_shape: Any, _instance: Optional[Any] = ...): ...
    @property
    def temperature(self): ...
    @property
    def logits(self): ...
    @property
    def probs(self): ...