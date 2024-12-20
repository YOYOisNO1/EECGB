import sys
sys.path.append('../')
from program_83 import starts_one_ends
def test_1():
    assert True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert starts_one_ends(1) == 1
def test_3():
    assert starts_one_ends(2) == 18
def test_4():
    assert starts_one_ends(3) == 180
def test_5():
    assert starts_one_ends(4) == 1800
def test_6():
    assert starts_one_ends(5) == 18000
def test_7():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"