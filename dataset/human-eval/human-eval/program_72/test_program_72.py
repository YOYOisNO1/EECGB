import sys
sys.path.append('../')
from program_72 import will_it_fly
def test_1():
    assert will_it_fly([3, 2, 3], 9) is True
def test_2():
    assert will_it_fly([1, 2], 5) is False
def test_3():
    assert will_it_fly([3], 5) is True
def test_4():
    assert will_it_fly([3, 2, 3], 1) is False
def test_5():
    assert will_it_fly([1, 2, 3], 6) is False
def test_6():
    assert will_it_fly([5], 5) is True