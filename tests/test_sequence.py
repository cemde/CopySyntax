from msilib import sequence
import sys
import os
import pyperclip

import pytest

# TODO fix importing literal_copy to delete this
# sys.path.append(os.path.join(os.getcwd(), "src"))
import literal_copy as lc

def test_bool_sequence():
    lengths = [0,2,3]
    dtypes = [bool, "bool", "bool"]
    sequences = [
        [],
        [True, False],
        [True, False, True],
    ]
    for l, dt, seq in zip(lengths, dtypes, sequences):
        synt = lc.sequence(l, dt)
        assert synt.print() == seq, f"test_bool_sequence failed: object: {synt} != {seq}"

