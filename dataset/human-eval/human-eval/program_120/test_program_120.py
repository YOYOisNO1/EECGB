import sys
sys.path.append('../')
from program_120 import maximum
def test_1():
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
def test_2():
    assert maximum([4, -4, 4], 2) == [4, 4]
def test_3():
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
def test_4():
    assert maximum([123, -123, 20, 0 , 1, 2, -3], 3) == [2, 20, 123]
def test_5():
    assert maximum([-123, 20, 0 , 1, 2, -3], 4) == [0, 1, 2, 20]
def test_6():
    assert maximum([5, 15, 0, 3, -13, -8, 0], 7) == [-13, -8, 0, 0, 3, 5, 15]
def test_7():
    assert maximum([-1, 0, 2, 5, 3, -10], 2) == [3, 5]
def test_8():
    assert maximum([1, 0, 5, -7], 1) == [5]
def test_9():
    assert maximum([4, -4], 2) == [-4, 4]
def test_10():
    assert maximum([-10, 10], 2) == [-10, 10]
def test_11():
    assert maximum([1, 2, 3, -23, 243, -400, 0], 0) == []