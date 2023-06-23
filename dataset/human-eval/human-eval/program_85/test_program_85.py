import sys
sys.path.append('../')
from program_85 import add
def test_1():
    assert add([4, 88]) == 88
def test_2():
    assert add([4, 5, 6, 7, 2, 122]) == 122
def test_3():
    assert add([4, 0, 6, 7]) == 0
def test_4():
    assert add([4, 4, 6, 8]) == 12