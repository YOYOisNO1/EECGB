import sys
sys.path.append('../')
from program_26 import remove_duplicates
def test_1():
    assert remove_duplicates([]) == []
def test_2():
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]
def test_3():
    assert remove_duplicates([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5]