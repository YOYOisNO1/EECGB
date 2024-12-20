import sys
sys.path.append('../')
from program_48 import is_palindrome
def test_1():
    assert is_palindrome('') == True
def test_2():
    assert is_palindrome('aba') == True
def test_3():
    assert is_palindrome('aaaaa') == True
def test_4():
    assert is_palindrome('zbcd') == False
def test_5():
    assert is_palindrome('xywyx') == True
def test_6():
    assert is_palindrome('xywyz') == False
def test_7():
    assert is_palindrome('xywzx') == False