import sys
sys.path.append('../')
from program_58 import common
def test_1():
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
def test_2():
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]
def test_3():
    assert common([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
def test_4():
    assert common([4, 3, 2, 8], []) == []