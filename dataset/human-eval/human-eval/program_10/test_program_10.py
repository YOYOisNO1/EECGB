import sys
sys.path.append('../')
from program_10 import is_palindrome
from program_10 import make_palindrome
def test_1():
    assert make_palindrome('') == ''
def test_2():
    assert make_palindrome('x') == 'x'
def test_3():
    assert make_palindrome('xyz') == 'xyzyx'
def test_4():
    assert make_palindrome('xyx') == 'xyx'
def test_5():
    assert make_palindrome('jerry') == 'jerryrrej'