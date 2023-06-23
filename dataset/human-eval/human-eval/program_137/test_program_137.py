import sys
sys.path.append('../')
from program_137 import compare_one
def test_1():
    assert compare_one(1, 2) == 2
def test_2():
    assert compare_one(1, 2.5) == 2.5
def test_3():
    assert compare_one(2, 3) == 3
def test_4():
    assert compare_one(5, 6) == 6
def test_5():
    assert compare_one(1, "2,3") == "2,3"
def test_6():
    assert compare_one("5,1", "6") == "6"
def test_7():
    assert compare_one("1", "2") == "2"
def test_8():
    assert compare_one("1", 1) == None
def test_9():
    assert True