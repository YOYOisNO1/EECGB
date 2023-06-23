import sys
sys.path.append('../')
from program_107 import even_odd_palindrome
def test_1():
    assert even_odd_palindrome(123) == (8, 13)
def test_2():
    assert even_odd_palindrome(12) == (4, 6)
def test_3():
    assert even_odd_palindrome(3) == (1, 2)
def test_4():
    assert even_odd_palindrome(63) == (6, 8)
def test_5():
    assert even_odd_palindrome(25) == (5, 6)
def test_6():
    assert even_odd_palindrome(19) == (4, 6)
def test_7():
    assert even_odd_palindrome(9) == (4, 5), "This prints if this assert fails 1 (good for debugging!)"
def test_8():
    assert even_odd_palindrome(1) == (0, 1), "This prints if this assert fails 2 (also good for debugging!)"