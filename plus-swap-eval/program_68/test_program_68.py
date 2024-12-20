import sys
sys.path.append('../')
from program_68 import pluck
def test_1():
    assert True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert pluck([4,2,3]) == [2, 1], "Error"
def test_3():
    assert pluck([1,2,3]) == [2, 1], "Error"
def test_4():
    assert pluck([]) == [], "Error"
def test_5():
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1], "Error"
def test_6():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
def test_7():
    assert pluck([1, 2, 3, 0, 5, 3]) == [0, 3], "Error"
def test_8():
    assert pluck([5, 4, 8, 4 ,8]) == [4, 1], "Error"
def test_9():
    assert pluck([7, 6, 7, 1]) == [6, 1], "Error"
def test_10():
    assert pluck([7, 9, 7, 1]) == [], "Error"