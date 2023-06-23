import sys
sys.path.append('../')
from program_163 import generate_integers
def test_1():
    assert generate_integers(2, 10) == [2, 4, 6, 8], "Test 1"
def test_2():
    assert generate_integers(10, 2) == [2, 4, 6, 8], "Test 2"
def test_3():
    assert generate_integers(132, 2) == [2, 4, 6, 8], "Test 3"
def test_4():
    assert generate_integers(17,89) == [], "Test 4"
def test_5():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"