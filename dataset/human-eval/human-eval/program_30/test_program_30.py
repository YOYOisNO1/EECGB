import sys
sys.path.append('../')
from program_30 import get_positive
def test_1():
    assert get_positive([-1, -2, 4, 5, 6]) == [4, 5, 6]
def test_2():
    assert get_positive([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 3, 9, 123, 1]
def test_3():
    assert get_positive([-1, -2]) == []
def test_4():
    assert get_positive([]) == []