import sys
sys.path.append('../')
from program_35 import max_element
def test_1():
    assert max_element([1, 2, 3]) == 3
def test_2():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124