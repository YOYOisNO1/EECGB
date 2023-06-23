import sys
sys.path.append('../')
from program_138 import is_equal_to_sum_even
def test_1():
    assert is_equal_to_sum_even(4) == False
def test_2():
    assert is_equal_to_sum_even(6) == False
def test_3():
    assert is_equal_to_sum_even(8) == True
def test_4():
    assert is_equal_to_sum_even(10) == True
def test_5():
    assert is_equal_to_sum_even(11) == False
def test_6():
    assert is_equal_to_sum_even(12) == True
def test_7():
    assert is_equal_to_sum_even(13) == False
def test_8():
    assert is_equal_to_sum_even(16) == True