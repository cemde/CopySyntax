from typing import Union, Any, List
import string


def sequence(length: int, type_: Union[type, str]) -> List[Any]:
    """Generates lists with sequences of specified data types.

    :param length: Length of the generated sequence.
    :type length: int
    :param type_: Data type of the generated sequence.
    :type type_: Union[type, str]
    :return: The generated sequence.
    :rtype: List[Any]
    """
    if length == 0:
        return []
    if type_ in ["str", str]:
        return _str_sequence(length)
    elif type_ in ["int", int]:
        return _int_sequence(length)
    elif type_ in ["float", float]:
        return _float_sequence(length)
    elif type_ in ["bool", bool]:
        return _bool_sequence(length)


# TODO streamline with utils.generator
def _str_sequence(length: int) -> List[str]:
    pool = lambda i: [x * i for x in list(string.ascii_letters)]
    n_pool = len(pool(1))
    result = []
    step = 1
    while 0 < length:
        if length // n_pool > 0:
            l = n_pool
        else:
            l = length % n_pool
        result.extend(pool(step)[:l])
        length -= l
        step += 1
    return result


def _int_sequence(length: int) -> List[int]:
    return [i for i in range(length)]


def _float_sequence(length: int) -> List[float]:
    return [float(i) for i in range(length)]


def _bool_sequence(length: int) -> List[bool]:
    return [bool((i + 1) % 2) for i in range(length)]
