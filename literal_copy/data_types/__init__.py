from ..utils.importer import _pkg_is_installed, _import_package_if_exists
from .atomic import _syntax_atomic
from .iterable import _syntax_iterable

if _pkg_is_installed("numpy"):
    from .numpy_types import _syntax_numpy
else:
    _syntax_numpy = None

__all__= [_syntax_iterable, _syntax_atomic]