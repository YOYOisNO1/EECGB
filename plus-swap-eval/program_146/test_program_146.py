import sys
sys.path.append('../')
from program_146 import specialFilter
def test_1():
    assert specialFilter([5, -2, 1, -5]) == 0  
def test_2():
    assert specialFilter([15, -73, 14, -15]) == 1
def test_3():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
def test_4():
    assert specialFilter([43, -12, 93, 125, 121, 109]) == 4
def test_5():
    assert specialFilter([71, -2, -33, 75, 21, 19]) == 3
def test_6():
    assert specialFilter([1]) == 0              
def test_7():
    assert specialFilter([]) == 0                   