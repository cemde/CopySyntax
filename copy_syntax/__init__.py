from .syntax import syntax
from .syntax_object import Syntax
from .syntax_like import syntax_like
from .sequence import sequence

pandas_prefix = "pd."
numpy_prefix = "np."
pytorch_prefix = "torch."


# class Setting:
#    def __init__(self, string) -> None:
#        self.string = string
# def set_prefix(package):

__all__ = [
    syntax,
    Syntax,
    syntax_like,
    sequence,
    pandas_prefix,
    numpy_prefix,
    pytorch_prefix,
]
