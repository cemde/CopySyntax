from typing import Any, Union, List, Optional

from .utils.iterable import _iterable
from .utils.generators import letters
from .literal import Literal
from .sequence import sequence
from .syntax import syntax

def syntax_like(
    obj: Any,
    quotes: str = "double",
    seperator_space: bool = True,
    raw: bool = False,
) -> Union[str, Literal]:
    # set correct quotes
    if quotes not in ["single", "double", "'", '"']:
        raise ValueError(f"Valid values are `single` and `double`. Not {quotes}")
    if quotes == "single":
        quotes = "'"
    elif quotes == "double":
        quotes = '"'
    
    if _iterable(obj):
        data_type = _assert_invariant_datatype(obj)
        val = _syntax_like_iterable(obj, quotes, seperator_space, data_type)
    else:
        raise NotImplementedError("`syntax_like` is not implemented for atomic data types.")
        # val = _syntax_atomic(obj, quotes)
    if raw:
        return val
    else:
        return Literal(val, type(obj))


# def _syntax_like_atomic(obj, quotes: str) -> str:
#     if isinstance(obj, bool):
#         val = "True"
#     elif isinstance(obj, int):
#         val = str(2)
#     elif isinstance(obj, str):
#         val = f"{quotes}" + letters(len(obj)) + f"{quotes}"
#     elif isinstance(obj, float):
#         val = str(0.123)
#     elif isinstance(obj, complex):
#         val = f"complex(0.0,-1.0)"
#     elif obj is None:
#         val = "None"
#     else:
#         raise NotImplementedError(f"Object type '{type(obj)}' not implemented.")
#     return val



def _syntax_like_iterable(obj, quotes: str, seperator_space: bool, element_type: Any) -> str:
    seperator = ", " if seperator_space else ","
    if isinstance(obj, list):
        elements = sequence(len(obj), element_type)
        elements = [syntax(val, quotes).raw() for val in elements]
        string = "[" + seperator.join(elements) + "]"
        
    elif isinstance(obj, dict):
        key_type, val_type = element_type
        keys, vals = sequence(len(obj), key_type), sequence(len(obj), val_type)
        after_colon = " " if seperator_space else ""
        elements = [
            f"{syntax(key, quotes).raw()}:{after_colon}{syntax(val, quotes, seperator_space=seperator_space).raw()}"
            for key, val in zip(keys, vals)
        ]
        string = "{" + seperator.join(elements) + "}"
        
    elif isinstance(obj, tuple):
        elements = sequence(len(obj), element_type)
        elements = [syntax(val, quotes).raw() for val in elements]
        string = "(" + seperator.join(elements) + ",)"
        
    elif isinstance(obj, set):
        elements = sequence(len(obj), element_type)
        elements = [syntax(val, quotes).raw() for val in elements]
        string = "{" + seperator.join(elements) + "}"
        
    else:
        raise NotImplementedError(f"Object type '{type(obj)}' not implemented.")
    return string


def _assert_invariant_datatype(obj):
    if isinstance(obj, (list, tuple)):
        element_type = type(obj[0])
        if not all(isinstance(x, element_type) for x in obj):
            _raise_unequal_data_types_error(obj)
    elif isinstance(obj, set):
        element_type = next(iter(obj))
        if not all(isinstance(x, element_type) for x in obj):
            _raise_unequal_data_types_error(obj)        
    elif isinstance(obj, dict):
        keys = list(obj.keys())
        vals = list(obj.values())
        key_type = type(keys[0])
        val_type = type(vals[0])
        if not all(isinstance(x, key_type) for x in keys):
            _raise_unequal_data_types_error(obj)
        if not all(isinstance(x, val_type) for x in vals):
            _raise_unequal_data_types_error(obj)
    return element_type


def _raise_unequal_data_types_error(obj):
    raise ValueError(f'`syntax_like` only supports `{obj.__class__.__name__}` with elements of a single data types.')
