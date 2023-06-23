import sys
sys.path.append('../')
from program_36 import fizz_buzz
def test_1():
    assert fizz_buzz(50) == 0
def test_2():
    assert fizz_buzz(78) == 2
def test_3():
    assert fizz_buzz(79) == 3
def test_4():
    assert fizz_buzz(100) == 3
def test_5():
    assert fizz_buzz(200) == 6
def test_6():
    assert fizz_buzz(4000) == 192
def test_7():
    assert fizz_buzz(10000) == 639
def test_8():
    assert fizz_buzz(100000) == 8026