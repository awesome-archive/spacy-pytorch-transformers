# Stubs for torch.distributions.kl (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .bernoulli import Bernoulli
from .beta import Beta
from .binomial import Binomial
from .categorical import Categorical
from .dirichlet import Dirichlet
from .distribution import Distribution
from .exp_family import ExponentialFamily
from .exponential import Exponential
from .gamma import Gamma
from .geometric import Geometric
from .gumbel import Gumbel
from .half_normal import HalfNormal
from .independent import Independent
from .laplace import Laplace
from .lowrank_multivariate_normal import LowRankMultivariateNormal, _batch_lowrank_logdet, _batch_lowrank_mahalanobis
from .multivariate_normal import MultivariateNormal, _batch_mahalanobis
from .normal import Normal
from .one_hot_categorical import OneHotCategorical
from .pareto import Pareto
from .poisson import Poisson
from .transformed_distribution import TransformedDistribution
from .uniform import Uniform
from .utils import _sum_rightmost
from typing import Any

def register_kl(type_p: Any, type_q: Any): ...

class _Match:
    types: Any = ...
    def __init__(self, *types: Any) -> None: ...
    def __eq__(self, other: Any): ...
    def __le__(self, other: Any): ...

def kl_divergence(p: Any, q: Any): ...
