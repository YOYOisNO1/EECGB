import sys
sys.path.append('../')
from program_123 import get_odd_collatz
def test_1():
    assert get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]
def test_2():
    assert get_odd_collatz(5) == [1, 5]
def test_3():
    assert get_odd_collatz(12) == [1, 3, 5], "This prints if this assert fails 1 (good for debugging!)"
def test_4():
    assert get_odd_collatz(1) == [1], "This prints if this assert fails 2 (also good for debugging!)"