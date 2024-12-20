import sys
sys.path.append('../')
from program_4 import mean_absolute_deviation
def test_1():
    assert abs(mean_absolute_deviation([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6
def test_2():
    assert abs(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
def test_3():
    assert abs(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6