import sys
sys.path.append('../')
from program_159 import eat
def test_1():
    assert True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert eat(5, 6, 10) == [11, 4], "Error"
def test_3():
    assert eat(4, 8, 9) == [12, 1], "Error"
def test_4():
    assert eat(1, 10, 10) == [11, 0], "Error"
def test_5():
    assert eat(2, 11, 5) == [7, 0], "Error"
def test_6():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
def test_7():
    assert eat(4, 5, 7) == [9, 2], "Error"
def test_8():
    assert eat(4, 5, 1) == [5, 0], "Error"