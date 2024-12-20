import sys
sys.path.append('../')
from program_125 import split_words
def test_1():
    assert split_words("Hello world!") == ["Hello","world!"]
def test_2():
    assert split_words("Hello,world!") == ["Hello","world!"]
def test_3():
    assert split_words("Hello world,!") == ["Hello","world,!"]
def test_4():
    assert split_words("Hello,Hello,world !") == ["Hello,Hello,world","!"]
def test_5():
    assert split_words("abcdef") == 3
def test_6():
    assert split_words("aaabb") == 2
def test_7():
    assert split_words("aaaBb") == 1
def test_8():
    assert split_words("") == 0