import sys
sys.path.append('../')
from program_71 import triangle_area
def test_1():
    assert triangle_area(3, 4, 5) == 6.00, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert triangle_area(1, 2, 10) == -1
def test_3():
    assert triangle_area(4, 8, 5) == 8.18
def test_4():
    assert triangle_area(2, 2, 2) == 1.73
def test_5():
    assert triangle_area(1, 2, 3) == -1
def test_6():
    assert triangle_area(10, 5, 7) == 16.25
def test_7():
    assert triangle_area(2, 6, 3) == -1
def test_8():
    assert triangle_area(1, 1, 1) == 0.43, "This prints if this assert fails 2 (also good for debugging!)"
def test_9():
    assert triangle_area(2, 2, 10) == -1