import sys
sys.path.append('../')
from program_143 import words_in_sentence
def test_1():
    assert words_in_sentence("This is a test") == "is"
def test_2():
    assert words_in_sentence("lets go for swimming") == "go for"
def test_3():
    assert words_in_sentence("there is no place available here") == "there is no place"
def test_4():
    assert words_in_sentence("Hi I am Hussein") == "Hi am Hussein"
def test_5():
    assert words_in_sentence("go for it") == "go for it"
def test_6():
    assert words_in_sentence("here") == ""
def test_7():
    assert words_in_sentence("here is") == "is"