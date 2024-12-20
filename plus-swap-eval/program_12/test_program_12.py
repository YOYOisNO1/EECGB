import sys
sys.path.append('../')
from program_12 import longest
def test_1():
    assert longest([]) == None
def test_2():
    assert longest(['x', 'y', 'z']) == 'x'
def test_3():
    assert longest(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz'