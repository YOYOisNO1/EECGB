import sys
sys.path.append('../')
from program_55 import fib
def test_1():
    assert fib(10) == 55
def test_2():
    assert fib(1) == 1
def test_3():
    assert fib(8) == 21
def test_4():
    assert fib(11) == 89
def test_5():
    assert fib(12) == 144