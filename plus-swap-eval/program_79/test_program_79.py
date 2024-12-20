import sys
sys.path.append('../')
from program_79 import decimal_to_binary
def test_1():
    assert decimal_to_binary(0) == "db0db"
def test_2():
    assert decimal_to_binary(32) == "db100000db"
def test_3():
    assert decimal_to_binary(103) == "db1100111db"
def test_4():
    assert decimal_to_binary(15) == "db1111db", "This prints if this assert fails 1 (good for debugging!)"
def test_5():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"