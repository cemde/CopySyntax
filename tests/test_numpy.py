from typing import Type
import numpy as np
import pytest

import literal_copy as lc


class UselessObject:
    def __init__(self) -> None:
        pass


def test_array():
    objects = [
        np.array([[4, 3, 1], [2, 5, 6]], dtype=np.uint8),
        np.array([[4, 3, 1], [2, 5, 6]], dtype=np.float64),
        np.array([[True, False], [False, True]], dtype=bool),
        np.array([["This", "test", "will"], ["pass", "easily", "today"]], dtype="<U20"),
    ]
    strings = [
        "np.array([[4, 3, 1], [2, 5, 6]], dtype=dtype('uint8'))",
        "np.array([[4.0, 3.0, 1.0], [2.0, 5.0, 6.0]], dtype=dtype('float64'))",
        "np.array([[True, False], [False, True]], dtype=dtype('bool'))",
        'np.array([["This", "test", "will"], ["pass", "easily", "today"]], dtype=dtype(\'str640\'))',
    ]
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_list failed: object: {synt} != {s}"


def test_array_raises_type_error():
    obj = np.array([UselessObject(), UselessObject()])
    with pytest.raises(TypeError) as excinfo:
        synt = lc.syntax(obj)
    (msg,) = excinfo.value.args
    assert msg == 'Numpy Arrays with dtype "object" are not supported.'
