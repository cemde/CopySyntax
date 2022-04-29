import sys
import os
import pyperclip

import pytest

# TODO fix importing literal_copy to delete this
# sys.path.append(os.path.join(os.getcwd(), "src"))
import copy_syntax as lc


def test_str_sequence():
    lengths = [2, 60]
    dtypes = [str, "str"]
    sequences = [
        ["a", "b"],
        [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "aa",
            "bb",
            "cc",
            "dd",
            "ee",
            "ff",
            "gg",
            "hh",
        ],
    ]
    for l, dt, seq in zip(lengths, dtypes, sequences):
        synt = lc.sequence(l, dt)
        assert synt == seq, f"test_str_sequence failed: object: {synt} != {seq}"


def test_int_sequence():
    lengths = [2, 5]
    dtypes = [int, "int"]
    sequences = [[0, 1], [0, 1, 2, 3, 4]]
    for l, dt, seq in zip(lengths, dtypes, sequences):
        synt = lc.sequence(l, dt)
        assert synt == seq, f"test_int_sequence failed: object: {synt} != {seq}"


def test_float_sequence():
    lengths = [2, 5]
    dtypes = [float, "float"]
    sequences = [[0.0, 1.0], [0.0, 1.0, 2.0, 3.0, 4.0]]
    for l, dt, seq in zip(lengths, dtypes, sequences):
        synt = lc.sequence(l, dt)
        assert synt == seq, f"test_int_sequence failed: object: {synt} != {seq}"


def test_bool_sequence():
    lengths = [2, 3]
    dtypes = [bool, "bool"]
    sequences = [
        [True, False],
        [True, False, True],
    ]
    for l, dt, seq in zip(lengths, dtypes, sequences):
        synt = lc.sequence(l, dt)
        assert synt == seq, f"test_bool_sequence failed: object: {synt} != {seq}"


def test_empty_sequence():
    res = lc.sequence(0, "bool")
    assert res == [], f"test_empty_sequence failed: object: {res} != {[]}"
