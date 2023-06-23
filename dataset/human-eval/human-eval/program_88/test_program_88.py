import sys
sys.path.append('../')
from program_88 import sort_array
def test_1():
    assert True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert sort_array([]) == [], "Error"
def test_3():
    assert sort_array([5]) == [5], "Error"
def test_4():
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5], "Error"
def test_5():
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0], "Error"
def test_6():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
def test_7():
    assert sort_array([2, 1]) == [1, 2], "Error"
def test_8():
    assert sort_array([15, 42, 87, 32 ,11, 0]) == [0, 11, 15, 32, 42, 87], "Error"
def test_9():
    assert sort_array([21, 14, 23, 11]) == [23, 21, 14, 11], "Error"