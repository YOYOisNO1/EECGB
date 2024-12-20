import sys
sys.path.append('../')
from program_13 import greatest_common_divisor
def test_1():
    assert greatest_common_divisor(3, 7) == 1
def test_2():
    assert greatest_common_divisor(10, 15) == 5
def test_3():
    assert greatest_common_divisor(49, 14) == 7
def test_4():
    assert greatest_common_divisor(144, 60) == 12