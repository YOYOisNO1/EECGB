import sys
sys.path.append('../')
from program_118 import get_closest_vowel
def test_1():
    assert get_closest_vowel("yogurt") == "u"
def test_2():
    assert get_closest_vowel("full") == "u"
def test_3():
    assert get_closest_vowel("easy") == ""
def test_4():
    assert get_closest_vowel("eAsy") == ""
def test_5():
    assert get_closest_vowel("ali") == ""
def test_6():
    assert get_closest_vowel("bad") == "a"
def test_7():
    assert get_closest_vowel("most") == "o"
def test_8():
    assert get_closest_vowel("ab") == ""
def test_9():
    assert get_closest_vowel("ba") == ""
def test_10():
    assert get_closest_vowel("quick") == ""
def test_11():
    assert get_closest_vowel("anime") == "i"
def test_12():
    assert get_closest_vowel("Asia") == ""
def test_13():
    assert get_closest_vowel("Above") == "o"
def test_14():
    assert True