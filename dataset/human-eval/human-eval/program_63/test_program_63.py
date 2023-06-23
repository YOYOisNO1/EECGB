import sys
sys.path.append('../')
from program_63 import fibfib
def test_1():
    assert fibfib(2) == 1
def test_2():
    assert fibfib(1) == 0
def test_3():
    assert fibfib(5) == 4
def test_4():
    assert fibfib(8) == 24
def test_5():
    assert fibfib(10) == 81
def test_6():
    assert fibfib(12) == 274
def test_7():
    assert fibfib(14) == 927