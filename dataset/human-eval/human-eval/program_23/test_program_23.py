import sys
sys.path.append('../')
from program_23 import strlen
def test_1():
    assert strlen('') == 0
def test_2():
    assert strlen('x') == 1
def test_3():
    assert strlen('asdasnakj') == 9