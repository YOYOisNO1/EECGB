import sys
sys.path.append('../')
from program_31 import is_prime
def test_1():
    assert is_prime(6) == False
def test_2():
    assert is_prime(101) == True
def test_3():
    assert is_prime(11) == True
def test_4():
    assert is_prime(13441) == True
def test_5():
    assert is_prime(61) == True
def test_6():
    assert is_prime(4) == False
def test_7():
    assert is_prime(1) == False
def test_8():
    assert is_prime(5) == True
def test_9():
    assert is_prime(11) == True
def test_10():
    assert is_prime(17) == True
def test_11():
    assert is_prime(5 * 17) == False
def test_12():
    assert is_prime(11 * 7) == False
def test_13():
    assert is_prime(13441 * 19) == False