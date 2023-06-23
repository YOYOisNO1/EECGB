import sys
sys.path.append('../')
from program_76 import is_simple_power
def test_1():
    assert is_simple_power(16, 2)== True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert is_simple_power(143214, 16)== False, "This prints if this assert fails 1 (good for debugging!)"
def test_3():
    assert is_simple_power(4, 2)==True, "This prints if this assert fails 1 (good for debugging!)"
def test_4():
    assert is_simple_power(9, 3)==True, "This prints if this assert fails 1 (good for debugging!)"
def test_5():
    assert is_simple_power(16, 4)==True, "This prints if this assert fails 1 (good for debugging!)"
def test_6():
    assert is_simple_power(24, 2)==False, "This prints if this assert fails 1 (good for debugging!)"
def test_7():
    assert is_simple_power(128, 4)==False, "This prints if this assert fails 1 (good for debugging!)"
def test_8():
    assert is_simple_power(12, 6)==False, "This prints if this assert fails 1 (good for debugging!)"
def test_9():
    assert is_simple_power(1, 1)==True, "This prints if this assert fails 2 (also good for debugging!)"
def test_10():
    assert is_simple_power(1, 12)==True, "This prints if this assert fails 2 (also good for debugging!)"