import sys
sys.path.append('../')
from program_46 import fib4
def test_1():
    assert fib4(5) == 4
def test_2():
    assert fib4(8) == 28
def test_3():
    assert fib4(10) == 104
def test_4():
    assert fib4(12) == 386