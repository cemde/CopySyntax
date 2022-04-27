from typing import Any

import numpy as np

#from ..literal import Literal
from ..syntax import syntax

_numeric_types = {
    np.int8, np.int16, np.int32, np.int64, np.int128, np.int256,
    np.uint8, np.uint16, np.uint32, np.uint64, np.uint128, np.uint256,
    np.float16, np.float32, np.float64, np.float128, np.float256
}

def _syntax_numpy(obj: np.ndarray, quotes: str = "double", seperator_space: bool = True) -> str:
    if obj.dtype in _numeric_types:
        val = np.arange(start=0, stop=obj.size).reshape(obj.shape)
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

_syntax_numpy(np.array([1.2, 3.4], dtype=np.float16))