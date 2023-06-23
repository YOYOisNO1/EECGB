import sys
sys.path.append('../')
from program_53 import add
def test_1():
    assert add(0, 1) == 1
def test_2():
    assert add(1, 0) == 1
def test_3():
    assert add(2, 3) == 5
def test_4():
    assert add(5, 7) == 12
def test_5():
    assert add(7, 5) == 12
def test_6():
    assert add(x, y) == x + y