import sys
sys.path.append('../')
from program_21 import rescale_to_unit
def test_1():
    assert rescale_to_unit([2.0, 49.9]) == [0.0, 1.0]
def test_2():
    assert rescale_to_unit([100.0, 49.9]) == [1.0, 0.0]
def test_3():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
def test_4():
    assert rescale_to_unit([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]
def test_5():
    assert rescale_to_unit([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]