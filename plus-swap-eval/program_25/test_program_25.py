import sys
sys.path.append('../')
from program_25 import factorize
def test_1():
    assert factorize(2) == [2]
def test_2():
    assert factorize(4) == [2, 2]
def test_3():
    assert factorize(8) == [2, 2, 2]
def test_4():
    assert factorize(3 * 19) == [3, 19]
def test_5():
    assert factorize(3 * 19 * 3 * 19) == [3, 3, 19, 19]
def test_6():
    assert factorize(3 * 19 * 3 * 19 * 3 * 19) == [3, 3, 3, 19, 19, 19]
def test_7():
    assert factorize(3 * 19 * 19 * 19) == [3, 19, 19, 19]
def test_8():
    assert factorize(3 * 2 * 3) == [2, 3, 3]