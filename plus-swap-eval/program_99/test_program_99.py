import sys
sys.path.append('../')
from program_99 import closest_integer
def test_1():
    assert closest_integer("10") == 10, "Test 1"
def test_2():
    assert closest_integer("14.5") == 15, "Test 2"
def test_3():
    assert closest_integer("-15.5") == -16, "Test 3"
def test_4():
    assert closest_integer("15.3") == 15, "Test 3"
def test_5():
    assert closest_integer("0") == 0, "Test 0"