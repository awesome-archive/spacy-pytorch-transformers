# Stubs for thinc.rates (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def decaying(base_rate: Any, decay: Any, t: int = ...) -> None: ...
def compounding(start: Any, stop: Any, compound: Any, t: float = ...) -> None: ...
def annealing(rate: Any, decay: Any, decay_steps: Any, t: float = ...) -> None: ...
def slanted_triangular(max_rate: Any, num_steps: Any, cut_frac: float = ..., ratio: int = ..., decay: int = ..., t: float = ...) -> None: ...
