import sys
sys.path.append('../')
from program_128 import prod_signs
def test_1():
    assert True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert prod_signs([1, 2, 2, -4]) == -9
def test_3():
    assert prod_signs([0, 1]) == 0
def test_4():
    assert prod_signs([1, 1, 1, 2, 3, -1, 1]) == -10
def test_5():
    assert prod_signs([]) == None
def test_6():
    assert prod_signs([2, 4,1, 2, -1, -1, 9]) == 20
def test_7():
    assert prod_signs([-1, 1, -1, 1]) == 4
def test_8():
    assert prod_signs([-1, 1, 1, 1]) == -4
def test_9():
    assert prod_signs([-1, 1, 1, 0]) == 0
def test_10():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"