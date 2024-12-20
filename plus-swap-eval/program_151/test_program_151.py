import sys
sys.path.append('../')
from program_151 import double_the_difference
def test_1():
    assert double_the_difference([]) == 0 , "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert double_the_difference([5, 4]) == 25 , "This prints if this assert fails 2 (good for debugging!)"
def test_3():
    assert double_the_difference([0.1, 0.2, 0.3]) == 0 , "This prints if this assert fails 3 (good for debugging!)"
def test_4():
    assert double_the_difference([-10, -20, -30]) == 0 , "This prints if this assert fails 4 (good for debugging!)"
def test_5():
    assert double_the_difference([-1, -2, 8]) == 0, "This prints if this assert fails 5 (also good for debugging!)"
def test_6():
    assert double_the_difference([0.2, 3, 5]) == 34, "This prints if this assert fails 6 (also good for debugging!)"
def test_7():
    lst = list(range(-99, 100, 2))
    odd_sum = sum([i**2 for i in lst if i%2!=0 and i > 0])
    assert double_the_difference(lst) == odd_sum , "This prints if this assert fails 7 (good for debugging!)"