import sys
import os

import pytest

# TODO fix importing literal_copy to delete this
# sys.path.append(os.path.join(os.getcwd()))
import literal_copy as lc


# int
def test_int():
    x, s = 23633, "2"
    synt = lc.syntax_like(x)
    assert synt.print() == s, f"test_int failed: object: {x} != {s}"


# float
def test_float():
    objects = [0.0, -44.1, 0.9999999999999999]
    strings = ["0.123", "0.123", "0.123"]
    for obj, s in zip(objects, strings):
        synt = lc.syntax_like(obj)
        assert synt.print() == s, f"test_float failed: object: {obj} != {s}"


# str
def test_str():
    objects = ["Aa<?!~~tÜÄÖ09", "", "None", "False", '"Test"', "'Test'", "a"*100]
    strings = ['\"ABCDEFGHIJKLM\"', '\"\"', '\"ABCD\"', '\"ABCDE\"', '\"ABCDEF\"', '\"ABCDEF\"', '\"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijkl\"']
    for obj, s in zip(objects, strings):
        synt = lc.syntax_like(obj)
        assert synt.print() == s, f"test_str failed: object: {obj} != {s}"


# bool
def test_bool():
    objects = [True, False]
    strings = ["True", "True"]
    for obj, s in zip(objects, strings):
        synt = lc.syntax_like(obj)
        assert synt.print() == s, f"test_bool failed: object: {obj} != {s}"


# NoneType
def test_nonetype():
    objects = [None]
    strings = ["None"]
    for obj, s in zip(objects, strings):
        synt = lc.syntax_like(obj)
        assert synt.print() == s, f"test_none failed: object: {obj} != {s}"


# Complex
def test_complex():
    objects = [complex(0, 0), complex(-99, -99), complex(1.056, 2.11)]
    strings = ["complex(0.0,-1.0)", "complex(0.0,-1.0)", "complex(0.0,-1.0)"]
    for obj, s in zip(objects, strings):
        synt = lc.syntax_like(obj)
        assert synt.print() == s, f"test_complex failed: object: {obj} != {s}"


# List
def test_list():
    # TODO add string longer than 26 characters
    objects = [
        [4, 3, 1],
        ["A", "aB", "9", "999~"],
        [1.,1.,3.,4.],
        [],
    ]
    strings = [
        "[0, 1, 2]",
        '["a", "b", "c", "d"]',
        '[0.0, 1.0, 2.0, 3.0]',
        '[]'
    ]
    for obj, s in zip(objects, strings):
        synt = lc.syntax_like(obj)
        assert synt.print() == s, f"test_complex failed: object: {synt} != {s}"


# dictionary
def test_dict():
    objects = [
        {4: 1, 3: "Bla", 1: None},
        {"A": False, "aB": True, "9": None, "999~": complex(0, 0)},
        {0: 5, 1: None, 2: [False, 0.99], 3: {"A": complex(-1, 0), "T": -1}},
    ]
    strings = [
        '{2: 2, 3: "Bla", 1: None}',
        '{"A": False, "aB": True, "9": None, "999~": complex(0.0,0.0)}',
        '{0: 5, 1: None, 2: [False, 0.99], 3: {"A": complex(-1.0,0.0), "T": -1}}',
    ]
    for obj, s in zip(objects, strings):
        synt = lc.syntax_like(obj, seperator_space=True)
        assert synt.print() == s, f"test_complex failed: object: {synt} != {s}"

# tuple
def test_tuple():
    objects = [
        (1,2,5),
        (0.,-4.2)
    ]
    strings = [
        "(0, 1, 2,)",
        "(0.0, 1.0,)",
    ]
    for obj, s in zip(objects, strings):
        synt = lc.syntax_like(obj, seperator_space=True)
        assert synt.print() == s, f"test_tuple failed: object: {synt} != {s}"

# set
def test_set():
    objects = [
        set([0.,1.3]),
        set([False, True]),
        set([])
    ]
    strings = [
        ["{0.0, 1.0}", "{1.0, 0.0}"],
        ["{True, False}", "{False, True}"],
        ["{}"],
    ]
    for obj, s in zip(objects, strings):
        synt = lc.syntax_like(obj, seperator_space=True)
        assert synt.print() in s, f"test_set failed: object: {synt} not in {s}"

@pytest.mark.xfail
def test_varying_types():
    pass

@pytest.mark.xfail
def test_unsupported_type():
    pass

test_set()