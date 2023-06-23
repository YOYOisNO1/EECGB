import sys
sys.path.append('../')
from program_8 import sum_product
def test_1():
    assert sum_product([]) == (0, 1)
def test_2():
    assert sum_product([1, 1, 1]) == (3, 1)
def test_3():
    assert sum_product([100, 0]) == (100, 0)
def test_4():
    assert sum_product([3, 5, 7]) == (3 + 5 + 7, 3 * 5 * 7)
def test_5():
    assert sum_product([10]) == (10, 10)