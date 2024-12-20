import sys
sys.path.append('../')
from program_64 import vowels_count
def test_1():
    assert vowels_count("abcde") == 2, "Test 1"
def test_2():
    assert vowels_count("Alone") == 3, "Test 2"
def test_3():
    assert vowels_count("key") == 2, "Test 3"
def test_4():
    assert vowels_count("bye") == 1, "Test 4"
def test_5():
    assert vowels_count("keY") == 2, "Test 5"
def test_6():
    assert vowels_count("bYe") == 1, "Test 6"
def test_7():
    assert vowels_count("ACEDY") == 3, "Test 7"
def test_8():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"