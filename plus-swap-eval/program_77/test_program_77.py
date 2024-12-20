import sys
sys.path.append('../')
from program_77 import iscube
def test_1():
    assert iscube(1) == True, "First test error: " + str(iscube(1))
def test_2():
    assert iscube(2) == False, "Second test error: " + str(iscube(2))
def test_3():
    assert iscube(-1) == True, "Third test error: " + str(iscube(-1))
def test_4():
    assert iscube(64) == True, "Fourth test error: " + str(iscube(64))
def test_5():
    assert iscube(180) == False, "Fifth test error: " + str(iscube(180))
def test_6():
    assert iscube(1000) == True, "Sixth test error: " + str(iscube(1000))
def test_7():
    assert iscube(0) == True, "1st edge test error: " + str(iscube(0))
def test_8():
    assert iscube(1729) == False, "2nd edge test error: " + str(iscube(1728))