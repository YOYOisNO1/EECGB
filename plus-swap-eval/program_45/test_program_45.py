import sys
sys.path.append('../')
from program_45 import triangle_area
def test_1():
    assert triangle_area(5, 3) == 7.5
def test_2():
    assert triangle_area(2, 2) == 2.0
def test_3():
    assert triangle_area(10, 8) == 40.0