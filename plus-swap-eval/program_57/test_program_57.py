import sys
sys.path.append('../')
from program_57 import monotonic
def test_1():
    assert monotonic([1, 2, 4, 10]) == True
def test_2():
    assert monotonic([1, 2, 4, 20]) == True
def test_3():
    assert monotonic([1, 20, 4, 10]) == False
def test_4():
    assert monotonic([4, 1, 0, -10]) == True
def test_5():
    assert monotonic([4, 1, 1, 0]) == True
def test_6():
    assert monotonic([1, 2, 3, 2, 5, 60]) == False
def test_7():
    assert monotonic([1, 2, 3, 4, 5, 60]) == True
def test_8():
    assert monotonic([9, 9, 9, 9]) == True