import sys
sys.path.append('../')
from program_43 import pairs_sum_to_zero
def test_1():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
def test_2():
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
def test_3():
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
def test_4():
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
def test_5():
    assert pairs_sum_to_zero([1]) == False
def test_6():
    assert pairs_sum_to_zero([-3, 9, -1, 3, 2, 30]) == True
def test_7():
    assert pairs_sum_to_zero([-3, 9, -1, 3, 2, 31]) == True
def test_8():
    assert pairs_sum_to_zero([-3, 9, -1, 4, 2, 30]) == False
def test_9():
    assert pairs_sum_to_zero([-3, 9, -1, 4, 2, 31]) == False