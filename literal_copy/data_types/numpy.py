from typing import Any

import numpy as np

from ..literal import Literal


def _syntax_numpy(obj: np.ndarray, quotes: str, seperator_space: bool) -> str:
    np.arange(start=0, stop=obj.size).reshape(obj.shape)
    if obj.dtype in np.float:
        pass
    if isinstance(obj, bool):
        val = "True" if obj else "False"
    elif isinstance(obj, int):
        val = str(obj)
    elif isinstance(obj, str):
        val = f"{quotes}" + obj + f"{quotes}"
    elif isinstance(obj, float):
        val = str(obj)
    elif isinstance(obj, complex):
        val = f"complex({obj.real},{obj.imag})"
    elif obj is None:
        val = "None"
    else:
        raise NotImplementedError(f"Object type '{type(obj)}' not implemented.")
    return val
