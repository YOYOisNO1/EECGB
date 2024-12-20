import sys
sys.path.append('../')
from program_34 import unique
def test_1():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]