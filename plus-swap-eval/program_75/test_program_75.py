import sys
sys.path.append('../')
from program_75 import is_multiply_prime
def test_1():
    assert is_multiply_prime(5) == False
def test_2():
    assert is_multiply_prime(30) == True
def test_3():
    assert is_multiply_prime(8) == True
def test_4():
    assert is_multiply_prime(10) == False
def test_5():
    assert is_multiply_prime(125) == True
def test_6():
    assert is_multiply_prime(3 * 5 * 7) == True
def test_7():
    assert is_multiply_prime(3 * 6 * 7) == False
def test_8():
    assert is_multiply_prime(9 * 9 * 9) == False
def test_9():
    assert is_multiply_prime(11 * 9 * 9) == False
def test_10():
    assert is_multiply_prime(11 * 13 * 7) == True