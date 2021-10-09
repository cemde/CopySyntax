from collections.abc import Iterable

from .literal import Literal
from .types import base

import six

def iterable(arg):
    return (
        isinstance(arg, Iterable) 
        and not isinstance(arg, six.string_types)
    )

def syntax(obj, quotes="single", line_length=-1, seperator_space=False, raw=False):
    if iterable(obj):
        val = _syntax_iterable(obj, quotes=quotes, line_length=line_length, seperator_space=seperator_space)
    else:
        val = _syntax_atomic(obj, quotes=quotes, line_length=line_length)
    #raise NotImplementedError(f"Type: {type(obj)} not supported")
    if raw:
        return val
    else:
        return Literal(val, None)
 
 
def _syntax_atomic(obj, quotes, line_length):
    if isinstance(obj, int):
        val = str(obj)
    elif isinstance(obj, str):
        val = '"' + obj + '"'
    elif isinstance(obj, bool):
        val = "True" if obj else "False"
    elif isinstance(obj, float):
        val = str(obj)
    elif isinstance(obj, complex):
        val = f'complex({obj.real},{obj.imag})'
    elif obj is None:
        val = "None"
    else:
        val = None
    return val


def _syntax_iterable(obj, quotes, line_length, seperator_space):
    seperator = ", " if seperator_space else ","
    if isinstance(obj, list):
        val = [syntax(element, raw=True) for element in obj]
        val = "[" + seperator.join(val) + "]"
    elif isinstance(obj, dict):
        val = [f"{syntax(key)}: {syntax(val, seperator_space=seperator_space)}" for key, val in obj.items()]
        val = "{" + seperator.join(val) + "}"
    elif isinstance(obj, tuple):
        val = [syntax(element) for element in obj]
        val = "(" + seperator.join(val) + ",)"
    elif isinstance(obj, set):
        val = [syntax(element) for element in obj]
        val = "{" + seperator.join(val) + "}"
    else:
        val = None
    return val
