import sys
sys.path.append('../')
from program_80 import is_happy
def test_1():
    assert is_happy("a") == False , "a"
def test_2():
    assert is_happy("aa") == False , "aa"
def test_3():
    assert is_happy("abcd") == True , "abcd"
def test_4():
    assert is_happy("aabb") == False , "aabb"
def test_5():
    assert is_happy("adb") == True , "adb"
def test_6():
    assert is_happy("xyy") == False , "xyy"
def test_7():
    assert is_happy("iopaxpoi") == True , "iopaxpoi"
def test_8():
    assert is_happy("iopaxioi") == False , "iopaxioi"