from typing import Any

import numpy as np

import literal_copy as lc

_numeric_types = set(
    [np.dtype(t) for t in [np.int8, np.int16, np.int32, np.int64, int,
    np.uint8, np.uint16, np.uint32, np.uint64, float,
    np.float16, np.float32, np.float64]]
)

_string_types = set([])

def _syntax_numpy(obj: np.ndarray, quotes: str = "double", seperator_space: bool = True) -> str:
    dtype = obj.dtype
    obj = obj.tolist()
    val = lc.syntax(obj)
    
    val = f"np.array({val}, dtype=dtype({dtype.name}))" 
    
    if obj.dtype in _numeric_types:
        val = np.arange(start=0, stop=obj.size).reshape(obj.shape).astype(obj.dtype)
    if obj.dtype == bool:
        val
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


def _syntax_like_numpy(obj: np.ndarray, quotes: str = "double", seperator_space: bool = True) -> str:
    if obj.dtype in _numeric_types:
        val = np.arange(start=0, stop=obj.size).reshape(obj.shape).astype(obj.dtype)
    if obj.dtype == bool:
        val 
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


