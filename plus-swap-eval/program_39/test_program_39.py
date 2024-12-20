import sys
sys.path.append('../')
from program_39 import prime_fib
def test_1():
    assert prime_fib(1) == 2
def test_2():
    assert prime_fib(2) == 3
def test_3():
    assert prime_fib(3) == 5
def test_4():
    assert prime_fib(4) == 13
def test_5():
    assert prime_fib(5) == 89
def test_6():
    assert prime_fib(6) == 233
def test_7():
    assert prime_fib(7) == 1597
def test_8():
    assert prime_fib(8) == 28657
def test_9():
    assert prime_fib(9) == 514229
def test_10():
    assert prime_fib(10) == 433494437