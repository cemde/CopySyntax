from typing import Any
import numpy as np

import copy_syntax as lc


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
    if obj.dtype.kind in {'f', 'i', 'u'}:
        val = np.arange(start=0, stop=obj.size)
    elif obj.dtype.kind in {'U', 'S'}:
        val = np.array(lc.sequence(obj.size, type_=str))
    elif obj.dtype.kind in {'b'}:
        val = np.array(lc.sequence(obj.size, type_=bool))
    else:
        raise TypeError(f'Numpy Arrays with dtype "{obj.dtype}" are not supported.')
    val = val.reshape(obj.shape).astype(obj.dtype)
    val = _syntax_numpy(val, quotes=quotes, seperator_space=seperator_space)
    return val
