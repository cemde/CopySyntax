from typing import Any, Union, List, Optional

from .utils.iterable import _iterable
from .utils.generators import letters
from .literal import Literal


def syntax_like(
    obj: Any,
    quotes: str = "double",
    line_length: int = -1,
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
        val = _syntax_like_iterable(
            obj, quotes=quotes, line_length=line_length, seperator_space=seperator_space
        )
    else:
        val = _syntax_like_atomic(obj, quotes=quotes, line_length=line_length)
    if raw:
        return val
    else:
        return Literal(val, type(obj))


def _syntax_like_atomic(obj, quotes: str, line_length: int) -> str:
    if isinstance(obj, bool):
        val = "True"
    elif isinstance(obj, int):
        val = str(2)
    elif isinstance(obj, str):
        val = f"{quotes}" + letters(len(obj)) + f"{quotes}"
    elif isinstance(obj, float):
        val = str(0.123)
    elif isinstance(obj, complex):
        val = f"complex(0.0,-1.0)"
    elif obj is None:
        val = "None"
    else:
        raise NotImplementedError(f"Object type '{type(obj)}' not implemented.")
    return val


def _syntax_like_iterable(obj, quotes: str, line_length: int, seperator_space: bool) -> str:
    seperator = ", " if seperator_space else ","
    if isinstance(obj, list):
        val = [syntax_like(element, raw=True) for element in obj]
        val = "[" + seperator.join(val) + "]"
    elif isinstance(obj, dict):
        val = [
            f"{syntax_like(key, raw=True)}: {syntax_like(val, seperator_space=seperator_space)}"
            for key, val in obj.items()
        ]
        val = "{" + seperator.join(val) + "}"
    elif isinstance(obj, tuple):
        val = [syntax_like(element, raw=True) for element in obj]
        val = "(" + seperator.join(val) + ",)"
    elif isinstance(obj, set):
        val = [syntax_like(element, raw=True) for element in obj]
        val = "{" + seperator.join(val) + "}"
    else:
        raise NotImplementedError(f"Object type '{type(obj)}' not implemented.")
    return val
