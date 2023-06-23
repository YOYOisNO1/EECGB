import sys
sys.path.append('../')
from program_6 import parse_nested_parens
def test_1():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
def test_2():
    assert parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4]
def test_3():
    assert parse_nested_parens('(()(())((())))') == [4]