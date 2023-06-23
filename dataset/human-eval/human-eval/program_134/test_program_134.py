import sys
sys.path.append('../')
from program_134 import check_if_last_char_is_a_letter
def test_1():
    assert check_if_last_char_is_a_letter("apple") == False
def test_2():
    assert check_if_last_char_is_a_letter("apple pi e") == True
def test_3():
    assert check_if_last_char_is_a_letter("eeeee") == False
def test_4():
    assert check_if_last_char_is_a_letter("A") == True
def test_5():
    assert check_if_last_char_is_a_letter("Pumpkin pie ") == False
def test_6():
    assert check_if_last_char_is_a_letter("Pumpkin pie 1") == False
def test_7():
    assert check_if_last_char_is_a_letter("") == False
def test_8():
    assert check_if_last_char_is_a_letter("eeeee e ") == False
def test_9():
    assert check_if_last_char_is_a_letter("apple pie") == False
def test_10():
    assert check_if_last_char_is_a_letter("apple pi e ") == False
def test_11():
    assert True