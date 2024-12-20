import sys
sys.path.append('../')
from program_52 import below_threshold
def test_1():
    assert below_threshold([1, 2, 4, 10], 100)
def test_2():
    assert not below_threshold([1, 20, 4, 10], 5)
def test_3():
    assert below_threshold([1, 20, 4, 10], 21)
def test_4():
    assert below_threshold([1, 20, 4, 10], 22)
def test_5():
    assert below_threshold([1, 8, 4, 10], 11)
def test_6():
    assert not below_threshold([1, 8, 4, 10], 10)