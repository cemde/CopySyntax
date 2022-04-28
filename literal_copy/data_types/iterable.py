


def _syntax_iterable(obj, quotes: str, seperator_space: bool) -> str:
    seperator = ", " if seperator_space else ","
    if isinstance(obj, list):
        elements = [syntax(val, quotes).raw() for val in obj]
        string = "[" + seperator.join(elements) + "]"
    elif isinstance(obj, dict):
        after_colon = " " if seperator_space else ""
        elements = [
            f"{syntax(key, quotes).raw()}:{after_colon}{syntax(val, quotes, seperator_space=seperator_space).raw()}"
            for key, val in obj.items()
        ]
        string = "{" + seperator.join(elements) + "}"
    elif isinstance(obj, tuple):
        elements = [syntax(val, quotes).raw() for val in obj]
        string = "(" + seperator.join(elements) + ",)"
    elif isinstance(obj, set):
        elements = [syntax(val, quotes).raw() for val in obj]
        string = "{" + seperator.join(elements) + "}"
    else:
        raise NotImplementedError(f"Object type '{type(obj)}' not implemented.")
    return string
