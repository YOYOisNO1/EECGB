import sys
sys.path.append('../')
from program_1 import separate_paren_groups

def test_1():
    assert separate_paren_groups('(()()) ((())) () ((())()())') ==  [
        '(()())', '((()))', '()', '((())()())'
    ]
def test_2():
    assert separate_paren_groups('() (()) ((())) (((())))') ==  [
        '()', '(())', '((()))', '(((())))'
    ]
def test_3():
    assert separate_paren_groups('(()(())((())))') == [
        '(()(())((())))'
    ]
def test_4():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']