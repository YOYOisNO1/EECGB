import sys
sys.path.append('../')
from program_127 import intersection
def test_1():
    assert intersection((1, 2), (2, 3)) == "NO"
def test_2():
    assert intersection((-1, 1), (0, 4)) == "NO"
def test_3():
    assert intersection((-3, -1), (-5, 5)) == "YES"
def test_4():
    assert intersection((-2, 2), (-4, 0)) == "YES"
def test_5():
    assert intersection((-11, 2), (-1, -1)) == "NO"
def test_6():
    assert intersection((1, 2), (3, 5)) == "NO"
def test_7():
    assert intersection((1, 2), (1, 2)) == "NO"
def test_8():
    assert intersection((-2, -2), (-3, -2)) == "NO"