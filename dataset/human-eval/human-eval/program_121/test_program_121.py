import sys
sys.path.append('../')
from program_121 import solution
def test_1():
    assert solution([5, 8, 7, 1])    == 12
def test_2():
    assert solution([3, 3, 3, 3, 3]) == 9
def test_3():
    assert solution([30, 13, 24, 321]) == 0
def test_4():
    assert solution([5, 9]) == 5
def test_5():
    assert solution([2, 4, 8]) == 0
def test_6():
    assert solution([30, 13, 23, 32]) == 23
def test_7():
    assert solution([3, 13, 2, 9]) == 3