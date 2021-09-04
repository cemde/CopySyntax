from collections.abc import Iterable

from .literal import Literal
from .types import base

import six

def iterable(arg):
    return (
        isinstance(arg, Iterable) 
        and not isinstance(arg, six.string_types)
    )

def syntax(obj, quotes="single", line_length=-1):
    if iterable(obj):
        val = base._syntax_iterable(obj, quotes=quotes, line_length=line_length)
    else:
        val = base._syntax_atomic(obj, quotes=quotes, line_length=line_length)
    #raise NotImplementedError(f"Type: {type(obj)} not supported")
    return Literal(val, None)
 