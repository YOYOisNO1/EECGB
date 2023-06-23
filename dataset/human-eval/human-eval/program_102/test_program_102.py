import sys
sys.path.append('../')
from program_102 import choose_num
def test_1():
    assert choose_num(12, 15) == 14
def test_2():
    assert choose_num(13, 12) == -1
def test_3():
    assert choose_num(33, 12354) == 12354
def test_4():
    assert choose_num(5234, 5233) == -1
def test_5():
    assert choose_num(6, 29) == 28
def test_6():
    assert choose_num(27, 10) == -1
def test_7():
    assert choose_num(7, 7) == -1
def test_8():
    assert choose_num(546, 546) == 546