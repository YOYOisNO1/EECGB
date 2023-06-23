import sys
sys.path.append('../')
from program_139 import special_factorial
def test_1():
    assert special_factorial(4) == 288, "Test 4"
def test_2():
    assert special_factorial(5) == 34560, "Test 5"
def test_3():
    assert special_factorial(7) == 125411328000, "Test 7"
def test_4():
    assert special_factorial(1) == 1, "Test 1"