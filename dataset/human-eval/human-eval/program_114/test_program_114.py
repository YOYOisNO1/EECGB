import sys
sys.path.append('../')
from program_114 import minSubArraySum
def test_1():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert minSubArraySum([-1, -2, -3]) == -6
def test_3():
    assert minSubArraySum([-1, -2, -3, 2, -10]) == -14
def test_4():
    assert minSubArraySum([-9999999999999999]) == -9999999999999999
def test_5():
    assert minSubArraySum([0, 10, 20, 1000000]) == 0
def test_6():
    assert minSubArraySum([-1, -2, -3, 10, -5]) == -6
def test_7():
    assert minSubArraySum([100, -1, -2, -3, 10, -5]) == -6
def test_8():
    assert minSubArraySum([10, 11, 13, 8, 3, 4]) == 3
def test_9():
    assert minSubArraySum([100, -33, 32, -1, 0, -2]) == -33
def test_10():
    assert minSubArraySum([-10]) == -10, "This prints if this assert fails 2 (also good for debugging!)"
def test_11():
    assert minSubArraySum([7]) == 7
def test_12():
    assert minSubArraySum([1, -1]) == -1