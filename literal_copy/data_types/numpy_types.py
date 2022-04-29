from typing import Any
import numpy as np

import literal_copy as lc


def _syntax_numpy(obj: np.ndarray, quotes: str = "double", seperator_space: bool = True) -> str:
    dtype = obj.dtype
    obj = obj.tolist()
    try:
        val = lc.syntax(obj, quotes=quotes, seperator_space=seperator_space)
    except TypeError:
        raise TypeError(f'Numpy Arrays with dtype "{dtype}" are not supported.')
    val = f"np.array({val}, dtype=dtype('{dtype.name}'))"
    return val


def _syntax_like_numpy(obj: np.ndarray, quotes: str = "double", seperator_space: bool = True) -> str:
    if obj.dtype.kind in {'f', 'i'}:
        val = np.arange(start=0, stop=obj.size).reshape(obj.shape).astype(obj.dtype)
        val = _syntax_numpy(val)
    elif obj.dtype.kind in {'U', 'S'}:
        val = np.array(lc.sequence(obj.size, type_=str)).reshape(obj.shape).astype(obj.dtype)
        val = _syntax_numpy(val)
    else:
        raise TypeError(f'Numpy Arrays with dtype "{obj.dtype}" are not supported.')
    return val
