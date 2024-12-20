import sys
sys.path.append('../')
from program_0 import has_close_elements
def test_1():
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
def test_2():
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
def test_3():
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
def test_4():
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
def test_5():
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
def test_6():
    assert has_close_elements([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True
def test_7():
    assert has_close_elements([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False