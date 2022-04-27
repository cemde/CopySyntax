from ..utils.importer import _pkg_is_installed, _import_package_if_exists

if _pkg_is_installed("numpy"):
    from .numpy_types import _syntax_numpy
else:
    _syntax_numpy = None
