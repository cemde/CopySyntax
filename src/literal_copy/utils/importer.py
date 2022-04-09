import importlib.util
import sys


def _pkg_is_installed(package_name):
    spec = importlib.util.find_spec(package_name)
    return spec is not None


# https://stackoverflow.com/questions/1051254/check-if-python-package-is-installed

# For illustrative purposes.
name = "itertools"


def _import_package_if_exists():
    if name in sys.modules:
        print(f"{name!r} already in sys.modules")
    elif (spec := importlib.util.find_spec(name)) is not None:
        # If you choose to perform the actual import ...
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        print(f"{name!r} has been imported")
    else:
        print(f"can't find the {name!r} module")
