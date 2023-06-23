import sys
sys.path.append('../')
from program_109 import move_one_ball
def test_1():
    assert move_one_ball([3, 4, 5, 1, 2])==True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert move_one_ball([3, 5, 10, 1, 2])==True
def test_3():
    assert move_one_ball([4, 3, 1, 2])==False
def test_4():
    assert move_one_ball([3, 5, 4, 1, 2])==False, "This prints if this assert fails 2 (also good for debugging!)"
def test_5():
    assert move_one_ball([])==True