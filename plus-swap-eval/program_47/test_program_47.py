import sys
sys.path.append('../')
from program_47 import median
def test_1():
    assert median([3, 1, 2, 4, 5]) == 3
def test_2():
    assert median([-10, 4, 6, 1000, 10, 20]) == 8.0
def test_3():
    assert median([5]) == 5
def test_4():
    assert median([6, 5]) == 5.5
def test_5():
    assert median([8, 1, 3, 9, 9, 2, 7]) == 7 