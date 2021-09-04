from collections.abc import Iterable
from literal_copy.syntax import syntax



# https://stackoverflow.com/questions/1051254/check-if-python-package-is-installed
# for checking if package is installed


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


def _syntax_iterable(obj, quotes, line_length):
    if isinstance(obj, list):
        val = [syntax(element) for element in obj]
        val = "[" + ",".join(val) + "]"
    elif isinstance(obj, dict):
        val = [f"{syntax(key)}: {syntax(val)}" for key, val in obj.items()]
        val = "{" + ",".join(val) + "}"
    elif isinstance(obj, tuple):
        val = [syntax(element) for element in obj]
        val = "(" + ",".join(val) + ",)"
    elif isinstance(obj, set):
        val = [syntax(element) for element in obj]
        val = "{" + ",".join(val) + "}"
    else:
        val = None
    return val


if __name__ == "__main__":
    print(syntax({'5': 1, 'blo': 4}))
    print(syntax((1, 5, 4,)))

