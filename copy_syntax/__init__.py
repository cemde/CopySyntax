from .syntax import syntax
from .literal import Literal
from .syntax_like import syntax_like
from .sequence import sequence

pandas_prefix = "pd."
numpy_prefix = "np."
pytorch_prefix = "torch."


# class Setting:
#    def __init__(self, string) -> None:
#        self.string = string
# def set_prefix(package):

__all__ = [syntax, Literal, syntax_like, sequence, pandas_prefix, numpy_prefix, pytorch_prefix]
