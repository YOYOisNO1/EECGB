import sys
sys.path.append('../')
from program_24 import largest_divisor
def test_1():
    assert largest_divisor(3) == 1
def test_2():
    assert largest_divisor(7) == 1
def test_3():
    assert largest_divisor(10) == 5
def test_4():
    assert largest_divisor(100) == 50
def test_5():
    assert largest_divisor(49) == 7