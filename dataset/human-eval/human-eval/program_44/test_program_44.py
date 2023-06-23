import sys
sys.path.append('../')
from program_44 import change_base
def test_1():
    assert change_base(8, 3) == "22"
def test_2():
    assert change_base(9, 3) == "100"
def test_3():
    assert change_base(234, 2) == "11101010"
def test_4():
    assert change_base(16, 2) == "10000"
def test_5():
    assert change_base(8, 2) == "1000"
def test_6():
    assert change_base(7, 2) == "111"
def test_7():
    assert change_base(x, x + 1) == str(x)