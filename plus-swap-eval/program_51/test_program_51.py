import sys
sys.path.append('../')
from program_51 import remove_vowels
def test_1():
    assert remove_vowels('') == ''
def test_2():
    assert remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'
def test_3():
    assert remove_vowels('fedcba') == 'fdcb'
def test_4():
    assert remove_vowels('eeeee') == ''
def test_5():
    assert remove_vowels('acBAA') == 'cB'
def test_6():
    assert remove_vowels('EcBOO') == 'cB'
def test_7():
    assert remove_vowels('ybcd') == 'ybcd'