import pytest

import copy_syntax as lc


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
    objects = ["Aa<?!~~tÜÄÖ09", "", "None", "False", '"Test"', "'Test'", "a" * 100]
    strings = [
        '"ABCDEFGHIJKLM"',
        '""',
        '"ABCD"',
        '"ABCDE"',
        '"ABCDEF"',
        '"ABCDEF"',
        '"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijkl"',
    ]
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
        [1.0, 1.0, 3.0, 4.0],
        [],
    ]
    strings = ["[0, 1, 2]", '["a", "b", "c", "d"]', "[0.0, 1.0, 2.0, 3.0]", "[]"]
    for obj, s in zip(objects, strings):
        synt = lc.syntax_like(obj)
        assert synt.print() == s, f"test_complex failed: object: {synt} != {s}"


# dictionary
def test_dict():
    objects = [
        {"A": 15, "T": 1},
        {},
        {1.2: True, 1.5: False},
    ]
    strings = [
        '{"a": 0, "b": 1}',
        "{}",
        "{0.0: True, 1.0: False}",
    ]
    for obj, s in zip(objects, strings):
        synt = lc.syntax_like(obj, seperator_space=True)
        assert synt.print() == s, f"test_complex failed: object: {synt} != {s}"


# tuple
def test_tuple():
    objects = [(1, 2, 5), (0.0, -4.2)]
    strings = [
        "(0, 1, 2,)",
        "(0.0, 1.0,)",
    ]
    for obj, s in zip(objects, strings):
        synt = lc.syntax_like(obj, seperator_space=True)
        assert synt.print() == s, f"test_tuple failed: object: {synt} != {s}"


# set
def test_set():
    objects = [set([0.0, 1.3]), set([False, True]), set([])]
    strings = [
        ["{0.0, 1.0}", "{1.0, 0.0}"],
        ["{True, False}", "{False, True}"],
        ["{}"],
    ]
    for obj, s in zip(objects, strings):
        synt = lc.syntax_like(obj, seperator_space=True)
        assert synt.print() in s, f"test_set failed: object: {synt} not in {s}"


@pytest.mark.parametrize("object", (["A", 1], {"A": 1, 2: 3}, {"B": 1, "C": False}))
def test_varying_types(object):
    with pytest.raises(ValueError) as excinfo:
        lc.syntax_like(object, seperator_space=True)
    (msg,) = excinfo.value.args
    assert msg == f"`syntax_like` only supports `{object.__class__.__name__}` with elements of a single data types."


@pytest.mark.xfail
def test_unsupported_type():
    # Implement test to make sure that iterables are not nested. dont allow list of List
    pass


test_varying_types({"B": 1, "C": False})
