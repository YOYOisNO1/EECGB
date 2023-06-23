import sys
sys.path.append('../')
from program_87 import get_row
def test_1():
    assert get_row([
def test_2():
    assert get_row([
def test_3():
    assert get_row([
def test_4():
    assert get_row([], 1) == []
def test_5():
    assert get_row([[1]], 2) == []
def test_6():
    assert get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
def test_7():
    assert True