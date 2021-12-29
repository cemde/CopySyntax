import sys
import os

# TODO fix importing literal_copy to delete this
sys.path.append(os.path.join(os.getcwd(), "src"))
import literal_copy as lc


# int
def test_int():
    objects = [-10, 0, 1, 23633]
    strings = ["-10", "0", "1", "23633"]
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_int failed: object: {synt} != {s}"


# float
def test_float():
    objects = [0.0, -44.1, 0.9999999999999999]
    strings = ["0.0", "-44.1", "0.9999999999999999"]
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_float failed: object: {synt} != {s}"


# str
def test_str():
    objects = ["Aa<?!~~tÜÄÖ09", "", "None", "False", '"Test"', "'Test'"]
    strings = [
        '"Aa<?!~~tÜÄÖ09"',
        '""',
        '"None"',
        '"False"',
        '""Test""',
        "\"'Test'\"",
    ]  # TODO think about how to mask quotes properly
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_str failed: object: {synt} != {s}"


# bool
def test_bool():
    objects = [True, False]
    strings = ["True", "False"]
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_bool failed: object: {synt} != {s}"


# NoneType
def test_nonetype():
    objects = [None]
    strings = ["None"]
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_none failed: object: {synt} != {s}"


# Complex
def test_complex():
    objects = [complex(0, 0), complex(-99, -99), complex(1.056, 2.11)]
    strings = ["complex(0.0,0.0)", "complex(-99.0,-99.0)", "complex(1.056,2.11)"]
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_complex failed: object: {synt} != {s}"


# list
def test_list():
    objects = [
        [4, 3, 1],
        ["A", "aB", "9", "999~"],
        ["qÄ", 5, None, [False, 0.99], complex(-1, 0)],
    ]
    strings = [
        "[4, 3, 1]",
        '["A", "aB", "9", "999~"]',
        '["qÄ", 5, None, [False, 0.99], complex(-1.0,0.0)]',
    ]
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj)
        assert synt.print() == s, f"test_list failed: object: {synt} != {s}"


# dict
def test_dict():
    objects = [
        {4: 1, 3: "Bla", 1: None},
        {"A": False, "aB": True, "9": None, "999~": complex(0, 0)},
        {0: 5, 1: None, 2: [False, 0.99], 3: {"A": complex(-1, 0), "T": -1}},
    ]
    strings = [
        '{4: 1, 3: "Bla", 1: None}',
        '{"A": False, "aB": True, "9": None, "999~": complex(0.0,0.0)}',
        '{0: 5, 1: None, 2: [False, 0.99], 3: {"A": complex(-1.0,0.0), "T": -1}}',
    ]
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj, seperator_space=True)
        assert synt.print() == s, f"test_dict failed: object: {synt} != {s}"


# tuple
def test_tuple():
    objects = [
        (1,2),
        (0,False,"A",-4.2)
    ]
    strings = [
        "(1, 2,)",
        "(0, False, \"A\", -4.2,)",
    ]
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj, seperator_space=True)
        assert synt.print() == s, f"test_tuple failed: object: {synt} != {s}"

# set
def test_set():
    objects = [
        set([0,1.3,"A"]),
        set([None, False, "False"]),
        set([])
    ]
    strings = [
        ["{0, 1.3, \"A\"}", "{0, \"A\", 1.3}", "{1.3, 0, \"A\"}", "{1.3, \"A\", 0}",  "{\"A\", 0, 1.3}", "{\"A\", 1.3, 0}"],
        ["{None, False, \"False\"}", "{None, \"False\", False}", "{False, None, \"False\"}", "{False, \"False\", None}",  "{\"False\", False, None}", "{\"False\", None, False}"],
        ["{}"],
    ]
    for obj, s in zip(objects, strings):
        synt = lc.syntax(obj, seperator_space=True)
        assert synt.print() in s, f"test_set failed: object: {synt} not in {s}"


# # test unkown object type
# def test_unkown_type():
#     class MyNonIterableType:
#         def __init__(self, s) -> None:
#             self.s = 5*s
    
#     class MyIterableType:
#         def __init__(self, s) -> None:
#             self.s = 5*s
#             assert False
    
#     objects = [MyNonIterableType(5), MyIterableType([1,2,3])]
#     for obj in objects:
#         synt = lc.syntax(obj, seperator_space=True)
#         # TODO catch error

      
# test single vs double quotes
def test_quotes():
    objects = [["A", "B"], ["A", "B"]]
    strings = ["['A', 'B']", '["A", "B"]']
    quotes = ["single", "double"]
    for obj, s, q in zip(objects, strings, quotes):
        synt = lc.syntax(obj, seperator_space=True, quotes=q)
        assert synt.print() == s, f"test_quotes failed: object: {synt} != {s}"

# test seperator space
def test_seperator():
    objects = [["A", "B"], ["A", "B"], {5:1, 2:["A","B"]}, {5:1, 2:["A","B"]}]
    strings = ['["A","B"]', '["A", "B"]', '{5:1,2:["A","B"]}', '{5: 1, 2: ["A", "B"]}']
    seperators = [False, True, False, True]
    for obj, s, sep in zip(objects, strings, seperators):
        synt = lc.syntax(obj, seperator_space=sep)
        assert synt.print() == s, f"test_seperator failed: object: {synt} != {s}"


# run tests
test_int()
test_float()
test_str()
test_bool()
test_nonetype()
test_complex()
test_list()
test_dict()
test_tuple()
test_set()
test_quotes()
test_seperator()

print("Done: All tests passed")
