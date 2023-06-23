import sys
sys.path.append('../')
from program_90 import next_smallest
def test_1():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
def test_2():
    assert next_smallest([5, 1, 4, 3, 2]) == 2
def test_3():
    assert next_smallest([]) == None
def test_4():
    assert next_smallest([1, 1]) == None
def test_5():
    assert next_smallest([1,1,1,1,0]) == 1
def test_6():
    assert next_smallest([1, 0**0]) == None
def test_7():
    assert next_smallest([-35, 34, 12, -45]) == -35
def test_8():
    assert True