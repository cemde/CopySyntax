import sys
import os

#TODO fix importing literal_copy to delete this
sys.path.append(os.path.join(os.getcwd(), 'src'))
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
    strings = ['[4,3,1]', '["A","aB","9","999~"]', '["qÄ",5,None,[False,0.99],complex(-1.0,0.0)]']
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_complex failed: object: {obj} != {s}"

def test_dict():
    objects = [{4: 1, 3: "Bla", 1: None},
               {"A": False, "aB": True, "9": None, "999~": complex(0,0)},
               {0: 5, 1: None, 2: [False, 0.99], 3: {"A": complex(-1,0), "T": -1}}]
    strings = ['{4: 1, 3: "Bla", 1: None}',
               '{"A": False, "aB": True, "9": None, "999~": complex(0.0,0.0)}',
               '{0: 5, 1: None, 2: [False, 0.99], 3: {"A": complex(-1.0,0.0), "T": -1}}']
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj, seperator_space=True)
        assert synt.print() == s, f"test_complex failed: object: {obj} != {s}"

def test_quotes():
    objects = [["A", "B"], ["A", "B"]]
    strings = ["['A', 'B']", "[\"A\", \"B\"]"]
    quotes = ["single", "double"]
    for obj, s, q in zip(objects, strings, quotes):
        synt = lc.syntax(obj, seperator_space=True, quotes=q)
        assert synt.print() == s, f"test_quotes failed: object: {obj} != {s}"

def test_seperator():
    objects = [["A", "B"], ["A", "B"]]
    strings = ["[\"A\",\"B\"]", "[\"A\", \"B\"]"]
    seperators = [False, True]
    for obj, s, sep in zip(objects, strings, seperators):
        synt = lc.syntax(obj, seperator_space=sep)
        assert synt.print() == s, f"test_quotes failed: object: {obj} != {s}"

        
# run tests 
test_int()
test_float()
test_str()
test_bool()
test_nonetype()
test_complex()
test_list()
test_dict()
test_quotes()
test_seperator()

print('Done: All tests passed')