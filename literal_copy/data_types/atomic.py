def _syntax_atomic(obj, quotes: str) -> str:
    if isinstance(obj, bool):
        val = "True" if obj else "False"
    elif isinstance(obj, int):
        val = str(obj)
    elif isinstance(obj, str):
        val = f"{quotes}" + obj + f"{quotes}"
    elif isinstance(obj, float):
        val = str(obj)
    elif isinstance(obj, complex):
        val = f"complex({obj.real},{obj.imag})"
    elif obj is None:
        val = "None"
    else:
        raise NotImplementedError(f"Object type '{type(obj)}' not implemented.")
    return val

__all__ = [_syntax_atomic]