from typing import Union, Any, List
import string


def sequence(length: int, type_: Union[type, str]) -> Any:
    if type_ in ["str", str]:
        return str_sequence(length)
    elif type_ in ["int", int]:
        return int_sequence(length)
    elif type_ in ["float", float]:
        return float_sequence(length)
    elif type_ in ["bool", bool]:
        return bool_sequence(length)
    
      
def str_sequence(length: int) -> List[str]:
    pool = lambda i: [x*i for x in list(string.ascii_letters)]
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


def int_sequence(length: int) -> List[int]:
    return [i for i in range(length)]


def float_sequence(length: int) -> List[float]:
    return [float(i) for i in range(length)]


def bool_sequence(length: int) -> List[bool]:
    return [bool((i+1) % 2) for i in range(length)]
    
