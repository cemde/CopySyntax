import copy_syntax as lc


def _syntax_iterable(obj, quotes: str, seperator_space: bool) -> str:
    seperator = ", " if seperator_space else ","
    if isinstance(obj, list):
        elements = [lc.syntax(val, quotes).raw() for val in obj]
        string = "[" + seperator.join(elements) + "]"
    elif isinstance(obj, dict):
        after_colon = " " if seperator_space else ""
        elements = [
            f"{lc.syntax(key, quotes).raw()}:"
            + f"{after_colon}{lc.syntax(val, quotes, seperator_space=seperator_space).raw()}"
            for key, val in obj.items()
        ]
        string = "{" + seperator.join(elements) + "}"
    elif isinstance(obj, tuple):
        elements = [lc.syntax(val, quotes).raw() for val in obj]
        string = "(" + seperator.join(elements) + ",)"
    elif isinstance(obj, set):
        elements = [lc.syntax(val, quotes).raw() for val in obj]
        string = "{" + seperator.join(elements) + "}"
    else:
        raise TypeError(f"Object type '{type(obj).__name__}' not supported.")
    return string
