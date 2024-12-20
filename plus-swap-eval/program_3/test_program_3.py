import sys
sys.path.append('../')
from program_3 import below_zero
def test_1():
    assert below_zero([]) == False
def test_2():
    assert below_zero([1, 2, -3, 1, 2, -3]) == False
def test_3():
    assert below_zero([1, 2, -4, 5, 6]) == True
def test_4():
    assert below_zero([1, -1, 2, -2, 5, -5, 4, -4]) == False
def test_5():
    assert below_zero([1, -1, 2, -2, 5, -5, 4, -5]) == True
def test_6():
    assert below_zero([1, -2, 2, -2, 5, -5, 4, -4]) == True