import sys
sys.path.append('../')
from program_154 import cycpattern_check
def test_1():
    assert True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
def test_3():
    assert  cycpattern_check("xyzw","xyw") == False , "test #0"
def test_4():
    assert  cycpattern_check("yello","ell") == True , "test #1"
def test_5():
    assert  cycpattern_check("whattup","ptut") == False , "test #2"
def test_6():
    assert  cycpattern_check("efef","fee") == True , "test #3"
def test_7():
    assert  cycpattern_check("abab","aabb") == False , "test #4"
def test_8():
    assert  cycpattern_check("winemtt","tinem") == True , "test #5"