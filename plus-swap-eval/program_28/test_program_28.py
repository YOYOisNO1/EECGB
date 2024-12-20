import sys
sys.path.append('../')
from program_28 import concatenate
def test_1():
    assert concatenate([]) == ''
def test_2():
    assert concatenate(['x', 'y', 'z']) == 'xyz'
def test_3():
    assert concatenate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk'