from typing import Any, Union

from .utils.iterable import _iterable
from .utils.generators import letters
from .syntax_object import Syntax
from .sequence import sequence
from .syntax import syntax
from .data_types import _syntax_like_numpy


def syntax_like(
    obj: Any,
    quotes: str = "double",
    seperator_space: bool = True,
    raw: bool = False,
) -> Union[str, Syntax]:
    """Creates an object of the same type and structure with preset values.

    .. code-block::
    :caption: A cool example

        The output of this line starts with four spaces.

    :param obj: Base Object
    :type obj: Any
    :param quotes: Quotes to use for generating string objects, defaults to "double"
    :type quotes: str, optional
    :param seperator_space: Whether to use spaces between elements in iterable objects, defaults to True
    :type seperator_space: bool, optional
    :param raw: if ``True`` returns a string object, defaults to False
    :type raw: bool, optional
    :raises ValueError: if the object is not supported.
    :return: The syntax to generate an object like the base object.
    :rtype: Union[str, Syntax]
    """
    # set correct quotes
    if quotes not in ["single", "double", "'", '"']:
        raise ValueError(f"Valid values are `single` and `double`. Not {quotes}")
    if quotes == "single":
        quotes = "'"
    elif quotes == "double":
        quotes = '"'

    try:
        import numpy as np

        if isinstance(obj, np.ndarray):
            val = _syntax_like_numpy(obj, quotes, seperator_space)
            return Syntax(val, str(type(obj)))

    except ModuleNotFoundError:
        pass

    if _iterable(obj):
        data_type = _assert_invariant_datatype(obj)
        val = _syntax_like_iterable(obj, quotes, seperator_space, data_type)
    else:
        # raise NotImplementedError("`syntax_like` is not implemented for atomic data types.")
        val = _syntax_like_atomic(obj, quotes)
    if raw:
        return val
    else:
        return Syntax(val, type(obj))


def _syntax_like_atomic(obj, quotes: str) -> str:
    if isinstance(obj, bool):
        val = "True"
    elif isinstance(obj, int):
        val = str(2)
    elif isinstance(obj, str):
        val = f"{quotes}" + letters(len(obj)) + f"{quotes}"
    elif isinstance(obj, float):
        val = str(0.123)
    elif isinstance(obj, complex):
        val = "complex(0.0,-1.0)"
    elif obj is None:
        val = "None"
    else:
        raise NotImplementedError(f"Object type '{type(obj)}' not supported.")
    return val


def _syntax_like_iterable(obj: Any, quotes: str, seperator_space: bool, element_type: Any) -> str:
    seperator = ", " if seperator_space else ","
    if isinstance(obj, list):
        elements = sequence(len(obj), element_type)
        elements = [syntax(val, quotes).raw() for val in elements]
        string = "[" + seperator.join(elements) + "]"

    elif isinstance(obj, dict):
        if element_type:
            key_type, val_type = element_type
            keys, vals = sequence(len(obj), key_type), sequence(len(obj), val_type)
            after_colon = " " if seperator_space else ""
            elements = [
                f"{syntax(key, quotes).raw()}:{after_colon}{syntax(val, quotes, seperator_space=seperator_space).raw()}"
                for key, val in zip(keys, vals)
            ]
        else:
            elements = []
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
    if not obj:
        return None
    if isinstance(obj, (list, tuple)):
        element_type = type(obj[0])
        if not all(isinstance(x, element_type) for x in obj):
            _raise_unequal_data_types_error(obj)
    elif isinstance(obj, set):
        element_type = type(next(iter(obj)))
        if not all(isinstance(x, element_type) for x in obj):
            _raise_unequal_data_types_error(obj)
    elif isinstance(obj, dict):
        keys = list(obj.keys())
        vals = list(obj.values())
        key_type = type(keys[0])
        val_type = type(vals[0])
        if not all(type(x) == key_type for x in keys):
            _raise_unequal_data_types_error(obj)
        if not all(type(x) == val_type for x in vals):
            _raise_unequal_data_types_error(obj)
        element_type = key_type, val_type
    return element_type


def _raise_unequal_data_types_error(obj):
    raise ValueError(f"`syntax_like` only supports `{obj.__class__.__name__}` with elements of a single data types.")
