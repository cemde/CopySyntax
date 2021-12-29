from typing import Any

from .utils.iterable import _iterable
from .literal import Literal


def syntax(
    obj: Any,
    quotes: str = "double",
    line_length: int = -1,
    seperator_space: bool = True,
) -> Literal:
    """Creates the string containing the syntax to recreate the same object. For example, with `a=["A",5]`
    using `syntax(a)` will generate '["A",5]' as a string to reproduce this variable in a different runtime.

    :param obj: The object for which the syntax should be generated. For types of objects supported see #TODO.
    :type obj: Any
    :param quotes: Sets quotes to signle or double quotes. Allowed values `single` or `double`, defaults to `double`
    :type quotes: str, optional
    :param line_length: Breaks up the syntax into multiple lines. Fo example, the syntax for a long list will be shown in multiple lines if it is longer
    than `line_length`, defaults to -1
    :type line_length: int, optional
    :param seperator_space: Decides wether a string will be placed between members of an interable. For example: `[4,5]` or `[4, 5]`, defaults to True
    :type seperator_space: bool, optional
    :return: Returns a syntax string, either as `str` or `Literal` object, depending on the `raw` argument.
    :rtype: Union[str, Literal]
    """
    # set correct quotes
    if quotes not in ["single", "double", "'", '"']:
        raise ValueError(f"Valid values are `single` and `double`. Not {quotes}")
    if quotes == "single":
        quotes = "'"
    elif quotes == "double":
        quotes = '"'

    if _iterable(obj):
        val = _syntax_iterable(obj, quotes, line_length, seperator_space)
    else:
        val = _syntax_atomic(obj, quotes, line_length)

    return Literal(val, str(type(obj)))


def _syntax_atomic(obj, quotes: str, line_length: int) -> str:
    if isinstance(obj, int):
        val = str(obj)
    elif isinstance(obj, str):
        val = f"{quotes}" + obj + f"{quotes}"
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
        elements = [syntax(val, quotes).raw() for val in obj]
        string = "[" + seperator.join(elements) + "]"
    elif isinstance(obj, dict):
        after_colon = " " if seperator_space else ""
        elements = [
            f"{syntax(key, quotes).raw()}:{after_colon}{syntax(val, quotes, seperator_space=seperator_space).raw()}"
            for key, val in obj.items()
        ]
        string = "{" + seperator.join(elements) + "}"
    elif isinstance(obj, tuple):
        elements = [syntax(val, quotes).raw() for val in obj]
        string = "(" + seperator.join(elements) + ",)"
    elif isinstance(obj, set):
        elements = [syntax(val, quotes).raw() for val in obj]
        string = "{" + seperator.join(elements) + "}"
    else:
        raise NotImplementedError(f"Object type '{type(obj)}' not implemented.")
    return string


#######################
###### Shortcuts ######
#######################

# s as short for syntax
def s(**kwargs):
    return syntax(**kwargs)

# sc as short for syntax to clipboard
def sc(**kwargs):
    syntax(**kwargs).clipboard()

# sp as short for syntax to print
def sp(**kwargs):
    syntax(**kwargs)