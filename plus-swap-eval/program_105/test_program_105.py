import sys
sys.path.append('../')
from program_105 import by_length
def test_1():
    assert True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"], "Error"
def test_3():
    assert by_length([]) == [], "Error"
def test_4():
    assert by_length([1, -1 , 55]) == ['One'], "Error"
def test_5():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
def test_6():
    assert by_length([1, -1, 3, 2]) == ["Three", "Two", "One"]
def test_7():
    assert by_length([9, 4, 8]) == ["Nine", "Eight", "Four"]