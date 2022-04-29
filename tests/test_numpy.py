import numpy as np
import pytest

import literal_copy as lc


def test_array():
    objects = [
        np.array([[4, 3, 1], [2,5,6]], dtype=np.uint8),
        #["A", "aB", "9", "999~"],
        #["qÄ", 5, None, [False, 0.99], complex(-1, 0)],
    ]
    strings = [
        "np.array([[4, 3, 1], [2,5,6]], dtype=dtype('uint8'))",
        #'["A", "aB", "9", "999~"]',
        #'["qÄ", 5, None, [False, 0.99], complex(-1.0,0.0)]',
    ]
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_list failed: object: {synt} != {s}"
