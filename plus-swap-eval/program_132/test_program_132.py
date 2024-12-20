import sys
sys.path.append('../')
from program_132 import is_nested
def test_1():
    assert is_nested('[[]]') == True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert is_nested('[]]]]]]][[[[[]') == False
def test_3():
    assert is_nested('[][]') == False
def test_4():
    assert is_nested(('[]')) == False
def test_5():
    assert is_nested('[[[[]]]]') == True
def test_6():
    assert is_nested('[]]]]]]]]]]') == False
def test_7():
    assert is_nested('[][][[]]') == True
def test_8():
    assert is_nested('[[]') == False
def test_9():
    assert is_nested('[]]') == False
def test_10():
    assert is_nested('[[]][[') == True
def test_11():
    assert is_nested('[[][]]') == True
def test_12():
    assert is_nested('') == False, "This prints if this assert fails 2 (also good for debugging!)"
def test_13():
    assert is_nested('[[[[[[[[') == False
def test_14():
    assert is_nested(']]]]]]]]') == False