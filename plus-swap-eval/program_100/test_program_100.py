import sys
sys.path.append('../')
from program_100 import make_a_pile
def test_1():
    assert make_a_pile(3) == [3, 5, 7], "Test 3"
def test_2():
    assert make_a_pile(4) == [4,6,8,10], "Test 4"
def test_3():
    assert make_a_pile(5) == [5, 7, 9, 11, 13]
def test_4():
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]
def test_5():
    assert make_a_pile(8) == [8, 10, 12, 14, 16, 18, 20, 22]
def test_6():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"