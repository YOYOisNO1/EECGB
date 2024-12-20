import sys
sys.path.append('../')
from program_49 import modp
def test_1():
    assert modp(3, 5) == 3
def test_2():
    assert modp(1101, 101) == 2
def test_3():
    assert modp(0, 101) == 1
def test_4():
    assert modp(3, 11) == 8
def test_5():
    assert modp(100, 101) == 1
def test_6():
    assert modp(30, 5) == 4
def test_7():
    assert modp(31, 5) == 3