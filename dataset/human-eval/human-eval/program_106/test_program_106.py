import sys
sys.path.append('../')
from program_106 import f
def test_1():
    assert f(5) == [1, 2, 6, 24, 15]
def test_2():
    assert f(7) == [1, 2, 6, 24, 15, 720, 28]
def test_3():
    assert f(1) == [1]
def test_4():
    assert f(3) == [1, 2, 6]