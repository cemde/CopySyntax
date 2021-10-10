# from typing import Any, Union, List, Optional

# from .utils.iterable import _iterable
# from .literal import Literal


# def syntax_like(
#     obj: Any,
#     quotes: str = "single",
#     line_length: int = -1,
#     seperator_space: bool = False,
#     raw: bool = False,
#     ) -> Union[str, Literal]:
#     if _iterable(obj):
#         val = _syntax_like_iterable(
#             obj, quotes=quotes, line_length=line_length, seperator_space=seperator_space
#         )
#     else:
#         val = _syntax_like_atomic(obj, quotes=quotes, line_length=line_length)
#     if raw:
#         return val
#     else:
#         return Literal(val, type(obj))


# def _syntax_like_atomic(obj, quotes: str, line_length: int) -> str:
#     if isinstance(obj, int):
#         val = str(1)
#     elif isinstance(obj, str):
#         l = len(obj)
#         val = '"a"*{l}'
#     elif isinstance(obj, bool):
#         val = "True"
#     elif isinstance(obj, float):
#         val = str(0.1)
#     elif isinstance(obj, complex):
#         val = f"complex({0},{1})"
#     elif obj is None:
#         val = "None"
#     else:
#         raise NotImplementedError(f"Object type '{type(obj)}' not implemented.")
#     return val


# #TODO
# def _syntax_like_iterable(obj, quotes: str, line_length: int, seperator_space: bool) -> str:
#     seperator = ", " if seperator_space else ","
#     if isinstance(obj, list):
#         val = [syntax_like(element, raw=True) for element in obj]
#         val = "[" + seperator.join(val) + "]"
#     elif isinstance(obj, dict):
#         val = [
#             f"{syntax_like(key)}: {syntax_like(val, seperator_space=seperator_space)}"
#             for key, val in obj.items()
#         ]
#         val = "{" + seperator.join(val) + "}"
#     elif isinstance(obj, tuple):
#         val = [syntax_like(element) for element in obj]
#         val = "(" + seperator.join(val) + ",)"
#     elif isinstance(obj, set):
#         val = [syntax_like(element) for element in obj]
#         val = "{" + seperator.join(val) + "}"
#     else:
#         raise NotImplementedError(f"Object type '{type(obj)}' not implemented.")
#     return val
