from typing import Any

from .utils.iterable import _iterable
from .literal import Literal
from .data_types import _syntax_numpy, _syntax_atomic, _syntax_iterable


def syntax(
    obj: Any,
    quotes: str = "double",
    seperator_space: bool = True,
) -> Literal:
    """Creates the string containing the syntax to recreate the same object. For example, with `a=["A",5]`
    using `syntax(a)` will generate '["A",5]' as a string to reproduce this variable in a different runtime.

    :param obj: The object for which the syntax should be generated. For types of objects supported see #TODO.
    :type obj: Any
    :param quotes: Sets quotes to signle or double quotes. Allowed values `single` or `double`, defaults to `double`
    :type quotes: str, optional
    :param seperator_space: Decides wether a string will be placed between members of an interable.
        For example: `[4,5]` or `[4, 5]`, defaults to True
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

    try:
        import numpy as np

        if isinstance(obj, np.ndarray):
            val = _syntax_numpy(obj, quotes, seperator_space)
            return Literal(val, str(type(obj)))

    except ModuleNotFoundError:
        pass

    if _iterable(obj):
        val = _syntax_iterable(obj, quotes, seperator_space)
    else:
        val = _syntax_atomic(obj, quotes)

    return Literal(val, str(type(obj)))


#######################  # noqa
###### Shortcuts ######  # noqa
#######################  # noqa

# s as short for syntax
def s(**kwargs):
    return syntax(**kwargs)


# sc as short for syntax to clipboard
def sc(**kwargs):
    syntax(**kwargs).clipboard()


# sp as short for syntax to print
def sp(**kwargs):
    syntax(**kwargs)
