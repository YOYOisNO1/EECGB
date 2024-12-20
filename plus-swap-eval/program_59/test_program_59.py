import sys
sys.path.append('../')
from program_59 import largest_prime_factor
def test_1():
    assert largest_prime_factor(15) == 5
def test_2():
    assert largest_prime_factor(27) == 3
def test_3():
    assert largest_prime_factor(63) == 7
def test_4():
    assert largest_prime_factor(330) == 11
def test_5():
    assert largest_prime_factor(13195) == 29