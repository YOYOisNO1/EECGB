import sys
sys.path.append('../')
from program_73 import smallest_change
def test_1():
    assert smallest_change([1,2,3,5,4,7,9,6]) == 4
def test_2():
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
def test_3():
    assert smallest_change([1, 4, 2]) == 1
def test_4():
    assert smallest_change([1, 4, 4, 2]) == 1
def test_5():
    assert smallest_change([1, 2, 3, 2, 1]) == 0
def test_6():
    assert smallest_change([3, 1, 1, 3]) == 0
def test_7():
    assert smallest_change([1]) == 0
def test_8():
    assert smallest_change([0, 1]) == 1