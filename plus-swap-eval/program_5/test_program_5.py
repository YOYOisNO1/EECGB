import sys
sys.path.append('../')
from program_5 import intersperse
def test_1():
    assert intersperse([], 7) == []
def test_2():
    assert intersperse([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2]
def test_3():
    assert intersperse([2, 2, 2], 2) == [2, 2, 2, 2, 2]