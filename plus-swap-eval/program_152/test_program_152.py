import sys
sys.path.append('../')
from program_152 import compare
def test_1():
    assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2])==[0,0,0,0,3,3], "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert compare([0,0,0,0,0,0],[0,0,0,0,0,0])==[0,0,0,0,0,0], "This prints if this assert fails 1 (good for debugging!)"
def test_3():
    assert compare([1,2,3],[-1,-2,-3])==[2,4,6], "This prints if this assert fails 1 (good for debugging!)"
def test_4():
    assert compare([1,2,3,5],[-1,2,3,4])==[2,0,0,1], "This prints if this assert fails 1 (good for debugging!)"
def test_5():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"