import sys
sys.path.append('../')
from program_160 import do_algebra
def test_1():
    assert do_algebra(['**', '*', '+'], [2, 3, 4, 5]) == 37
def test_2():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
def test_3():
    assert do_algebra(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"
def test_4():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"