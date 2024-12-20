import sys
sys.path.append('../')
from program_54 import same_chars
def test_1():
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
def test_2():
    assert same_chars('abcd', 'dddddddabc') == True
def test_3():
    assert same_chars('dddddddabc', 'abcd') == True
def test_4():
    assert same_chars('eabcd', 'dddddddabc') == False
def test_5():
    assert same_chars('abcd', 'dddddddabcf') == False
def test_6():
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') == False
def test_7():
    assert same_chars('aabb', 'aaccc') == False