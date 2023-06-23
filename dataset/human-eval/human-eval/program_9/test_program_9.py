import sys
sys.path.append('../')
from program_9 import rolling_max
def test_1():
    assert rolling_max([]) == []
def test_2():
    assert rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4]
def test_3():
    assert rolling_max([4, 3, 2, 1]) == [4, 4, 4, 4]
def test_4():
    assert rolling_max([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]