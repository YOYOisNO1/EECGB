import sys
sys.path.append('../')
from program_66 import digitSum
def test_1():
    assert True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert digitSum("") == 0, "Error"
def test_3():
    assert digitSum("abAB") == 131, "Error"
def test_4():
    assert digitSum("abcCd") == 67, "Error"
def test_5():
    assert digitSum("helloE") == 69, "Error"
def test_6():
    assert digitSum("woArBld") == 131, "Error"
def test_7():
    assert digitSum("aAaaaXa") == 153, "Error"
def test_8():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
def test_9():
    assert digitSum(" How are yOu?") == 151, "Error"
def test_10():
    assert digitSum("You arE Very Smart") == 327, "Error"