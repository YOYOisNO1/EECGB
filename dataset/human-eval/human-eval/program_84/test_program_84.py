import sys
sys.path.append('../')
from program_84 import solve
def test_1():
    assert True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert solve(1000) == "1", "Error"
def test_3():
    assert solve(150) == "110", "Error"
def test_4():
    assert solve(147) == "1100", "Error"
def test_5():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
def test_6():
    assert solve(333) == "1001", "Error"
def test_7():
    assert solve(963) == "10010", "Error"