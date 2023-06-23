import sys
sys.path.append('../')
from program_101 import words_string
def test_1():
    assert True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
def test_3():
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
def test_4():
    assert words_string("Hi, my name") == ["Hi", "my", "name"]
def test_5():
    assert words_string("One,, two, three, four, five, six,") == ["One", "two", "three", "four", "five", "six"]
def test_6():
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
def test_7():
    assert words_string("") == []
def test_8():
    assert words_string("ahmed     , gamal") == ["ahmed", "gamal"]