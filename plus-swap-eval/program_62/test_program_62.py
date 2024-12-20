import sys
sys.path.append('../')
from program_62 import derivative
def test_1():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
def test_2():
    assert derivative([1, 2, 3]) == [2, 6]
def test_3():
    assert derivative([3, 2, 1]) == [2, 2]
def test_4():
    assert derivative([3, 2, 1, 0, 4]) == [2, 2, 0, 16]
def test_5():
    assert derivative([1]) == []