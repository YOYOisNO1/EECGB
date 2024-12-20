import sys
sys.path.append('../')
from program_2 import truncate_number

def test_1():
    assert truncate_number(3.5) == 0.5
def test_2():
    assert abs(truncate_number(1.33) - 0.33) < 1e-6
def test_3():
    assert abs(truncate_number(123.456) - 0.456) < 1e-6