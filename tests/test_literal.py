import sys
import os
import pyperclip

#TODO fix importing literal_copy to delete this
sys.path.append(os.path.join(os.getcwd(), 'src'))
import literal_copy as lc

SYNTAX = '[4,5,"A",(5,False)]'
TYPE = 'List'
LITERAL = lc.Literal(SYNTAX, TYPE)

def test___str__(capsys):
    print(LITERAL)
    captured = capsys.readouterr()
    assert captured.out == SYNTAX + "\n"

def test_print():
    captured = LITERAL.print()
    assert captured == SYNTAX
    

def test_clipboard():
    LITERAL.clipboard()
    captured = pyperclip.paste()
    assert captured == SYNTAX

def test_save():
    file_path = 'tests/.test_literal_save.txt'
    
    # save to file if it does not exist
    if not os.path.isfile(file_path):
        LITERAL.save(file_path)
    else:
        raise OSError("Test file location '{file_path}' exists already.")
    
    # read from file
    with open(file_path, 'r') as f:
        captured = f.read()
    
    # delete file
    os.remove(file_path)
    
    # assert
    assert captured == SYNTAX

def test_save():
    file_path = 'tests/.test_literal_save.txt'
    
    #TODO
    #create a file existing in this location and then cathc the OSError    