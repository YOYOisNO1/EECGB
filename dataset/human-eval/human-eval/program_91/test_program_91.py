import sys
sys.path.append('../')
from program_91 import is_bored
def test_1():
    assert is_bored("Hello world") == 0, "Test 1"
def test_2():
    assert is_bored("Is the sky blue?") == 0, "Test 2"
def test_3():
    assert is_bored("I love It !") == 1, "Test 3"
def test_4():
    assert is_bored("bIt") == 0, "Test 4"
def test_5():
    assert is_bored("I feel good today. I will be productive. will kill It") == 2, "Test 5"
def test_6():
    assert is_bored("You and I are going for a walk") == 0, "Test 6"
def test_7():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"