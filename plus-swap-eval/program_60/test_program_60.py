import sys
sys.path.append('../')
from program_60 import sum_to_n
def test_1():
    assert sum_to_n(1) == 1
def test_2():
    assert sum_to_n(6) == 21
def test_3():
    assert sum_to_n(11) == 66
def test_4():
    assert sum_to_n(30) == 465
def test_5():
    assert sum_to_n(100) == 5050