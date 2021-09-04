import sys
import os

sys.path.append(os.path.join(os.getcwd()))

import literal_copy as lc

# int
def test_int():
    x, s = 23633, "23633"
    synt = lc.syntax(x)
    assert synt.print() == s, f"test_int failed: object: {x} != {s}"


# float
def test_float():
    objects = [0., -44.1, 0.9999999999999999]
    strings = ["0.0", "-44.1", "0.9999999999999999"]
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_float failed: object: {obj} != {s}"

# str
def test_str():
    objects = ['Aa<?!~~tÜÄÖ09', '', 'None', 'False', '"Test"', '\'Test\'']
    strings = ['"Aa<?!~~tÜÄÖ09"', '""', '"None"', '"False"', '""Test""', '"\'Test\'"'] #TODO think about how to mask quotes properly
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_str failed: object: {obj} != {s}"

# bool
def test_bool():
    objects = [True, False]
    strings = ['True', 'False']
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_bool failed: object: {obj} != {s}"

# NoneType
def test_nonetype():
    objects = [None]
    strings = ['None']
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_none failed: object: {obj} != {s}"

# Complex
def test_complex():
    objects = [complex(0,0), complex(-99,-99), complex(1.056,2.11)]
    strings = ['complex(0.0,0.0)', 'complex(-99.0,-99.0)', 'complex(1.056,2.11)']
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_complex failed: object: {obj} != {s}"

def test_list():
    objects = [[4,3,1], ["A", "aB", "9", "999~"], ["qÄ", 5, None, [False, 0.99], complex(-1,0)]]
    strings = ['[4,3,1]', '["A", "aB", "9", "999~"]', '["qÄ", 5, None, [False, 0.99], complex(-1,0)]']
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_complex failed: object: {obj} != {s}"


# def _syntax_iterable(obj, quotes, line_length):
#     if isinstance(obj, list):
#         val = [syntax(element) for element in obj]
#         val = "[" + ",".join(val) + "]"
#     elif isinstance(obj, dict):
#         val = [f"{syntax(key)}: {syntax(val)}" for key, val in obj.items()]
#         val = "{" + ",".join(val) + "}"
#     elif isinstance(obj, tuple):
#         val = [syntax(element) for element in obj]
#         val = "(" + ",".join(val) + ",)"
#     elif isinstance(obj, set):
#         val = [syntax(element) for element in obj]
#         val = "{" + ",".join(val) + "}"
#     else:
#         val = None
#     return val



# run tests 
test_int()
test_float()
test_str()
test_bool()
test_nonetype()
test_complex()
test_list()

print('Done: All tests passed')