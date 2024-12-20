import sys
sys.path.append('../')
from program_131 import digits
def test_1():
    assert digits(5) == 5
def test_2():
    assert digits(54) == 5
def test_3():
    assert digits(120) ==1
def test_4():
    assert digits(5014) == 5
def test_5():
    assert digits(98765) == 315
def test_6():
    assert digits(5576543) == 2625
def test_7():
    assert digits(2468) == 0