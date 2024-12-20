import sys
sys.path.append('../')
from program_115 import max_fill
def test_1():
    assert True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6, "Error"
def test_3():
    assert max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5, "Error"
def test_4():
    assert max_fill([[0,0,0], [0,0,0]], 5) == 0, "Error"
def test_5():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
def test_6():
    assert max_fill([[1,1,1,1], [1,1,1,1]], 2) == 4, "Error"
def test_7():
    assert max_fill([[1,1,1,1], [1,1,1,1]], 9) == 2, "Error"