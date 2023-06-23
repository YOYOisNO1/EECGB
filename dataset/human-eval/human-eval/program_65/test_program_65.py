import sys
sys.path.append('../')
from program_65 import circular_shift
def test_1():
    assert circular_shift(100, 2) == "001"
def test_2():
    assert circular_shift(12, 2) == "12"
def test_3():
    assert circular_shift(97, 8) == "79"
def test_4():
    assert circular_shift(12, 1) == "21", "This prints if this assert fails 1 (good for debugging!)"
def test_5():
    assert circular_shift(11, 101) == "11", "This prints if this assert fails 2 (also good for debugging!)"