import sys
sys.path.append('../')
from program_119 import match_parens
def test_1():
    assert match_parens(['()(', ')']) == 'Yes'
def test_2():
    assert match_parens([')', ')']) == 'No'
def test_3():
    assert match_parens(['(()(())', '())())']) == 'No'
def test_4():
    assert match_parens([')())', '(()()(']) == 'Yes'
def test_5():
    assert match_parens(['(())))', '(()())((']) == 'Yes'
def test_6():
    assert match_parens(['()', '())']) == 'No'
def test_7():
    assert match_parens(['(()(', '()))()']) == 'Yes'
def test_8():
    assert match_parens(['((((', '((())']) == 'No'
def test_9():
    assert match_parens([')(()', '(()(']) == 'No'
def test_10():
    assert match_parens([')(', ')(']) == 'No'
def test_11():
    assert match_parens(['(', ')']) == 'Yes'
def test_12():
    assert match_parens([')', '(']) == 'Yes' 