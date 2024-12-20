import sys
sys.path.append('../')
from program_108 import count_nums
def test_1():
    assert count_nums([]) == 0
def test_2():
    assert count_nums([-1, -2, 0]) == 0
def test_3():
    assert count_nums([1, 1, 2, -2, 3, 4, 5]) == 6
def test_4():
    assert count_nums([1, 6, 9, -6, 0, 1, 5]) == 5
def test_5():
    assert count_nums([1, 100, 98, -7, 1, -1]) == 4
def test_6():
    assert count_nums([12, 23, 34, -45, -56, 0]) == 5
def test_7():
    assert count_nums([-0, 1**0]) == 1
def test_8():
    assert count_nums([1]) == 1
def test_9():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"