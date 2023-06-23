import sys
sys.path.append('../')
from program_155 import even_odd_count
def test_1():
    assert even_odd_count(7) == (0, 1)
def test_2():
    assert even_odd_count(-78) == (1, 1)
def test_3():
    assert even_odd_count(3452) == (2, 2)
def test_4():
    assert even_odd_count(346211) == (3, 3)
def test_5():
    assert even_odd_count(-345821) == (3, 3)
def test_6():
    assert even_odd_count(-2) == (1, 0)
def test_7():
    assert even_odd_count(-45347) == (2, 3)
def test_8():
    assert even_odd_count(0) == (1, 0)
def test_9():
    assert True