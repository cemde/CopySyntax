from typing import Any, Union, List, Optional

from collections.abc import Iterable

from .literal import Literal
from .types import base

import six


def iterable(arg: Any) -> bool:
    return isinstance(arg, Iterable) and not isinstance(arg, six.string_types)


def syntax(
    obj: Any,
    quotes: str = "single",
    line_length: int = -1,
    seperator_space: bool = False,
    raw: bool = False,
    ) -> Union[str, Literal]:
    """Creates the string containing the syntax to recreate the same object. For example, with `a=["A",5]`
    using `syntax(a)` will generate '["A",5]' as a string to reproduce this variable in a different runtime.

    :param obj: The object for which the syntax should be generated. For types of objects supported see #TODO.
    :type obj: Any
    :param quotes: Sets quotes to signle or double quotes. Allowed values `'` or `"`, defaults to "single"
    :type quotes: str, optional
    :param line_length: Breaks up the syntax into multiple lines. Fo example, the syntax for a long list will be shown in multiple lines if it is longer
    than `line_length`, defaults to -1
    :type line_length: int, optional
    :param seperator_space: Decides wether a string will be placed between members of an interable. For example: `[4,5]` or `[4, 5]`, defaults to False
    :type seperator_space: bool, optional
    :param raw: If set to `False`, the function will return the raw string to generate the syntax. If `True` a `Literal` object will be
    returned that provides a simple syntax for copying or saving the syntax string, defaults to False
    :type raw: bool, optional
    :return: Returns a syntax string, either as `str` or `Literal` object, depending on the `raw` argument.
    :rtype: Union[str, Literal]
    """
    if iterable(obj):
        val = _syntax_iterable(
            obj, quotes=quotes, line_length=line_length, seperator_space=seperator_space
        )
    else:
        val = _syntax_atomic(obj, quotes=quotes, line_length=line_length)
    # raise NotImplementedError(f"Type: {type(obj)} not supported")
    if raw:
        return val
    else:
        return Literal(val, type(obj))


def _syntax_atomic(obj, quotes: str, line_length: int) -> str:
    if isinstance(obj, int):
        val = str(obj)
    elif isinstance(obj, str):
        val = '"' + obj + '"'
    elif isinstance(obj, bool):
        val = "True" if obj else "False"
    elif isinstance(obj, float):
        val = str(obj)
    elif isinstance(obj, complex):
        val = f"complex({obj.real},{obj.imag})"
    elif obj is None:
        val = "None"
    else:
        raise NotImplementedError(f"Object type '{type(obj)}' not implemented.")
    return val


def _syntax_iterable(obj, quotes: str, line_length: int, seperator_space: bool) -> str:
    seperator = ", " if seperator_space else ","
    if isinstance(obj, list):
        val = [syntax(element, raw=True) for element in obj]
        val = "[" + seperator.join(val) + "]"
    elif isinstance(obj, dict):
        val = [
            f"{syntax(key)}: {syntax(val, seperator_space=seperator_space)}"
            for key, val in obj.items()
        ]
        val = "{" + seperator.join(val) + "}"
    elif isinstance(obj, tuple):
        val = [syntax(element) for element in obj]
        val = "(" + seperator.join(val) + ",)"
    elif isinstance(obj, set):
        val = [syntax(element) for element in obj]
        val = "{" + seperator.join(val) + "}"
    else:
        raise NotImplementedError(f"Object type '{type(obj)}' not implemented.")
    return val
