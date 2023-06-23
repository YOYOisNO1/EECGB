import sys
sys.path.append('../')
from program_14 import all_prefixes
def test_1():
    assert all_prefixes('') == []
def test_2():
    assert all_prefixes('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
def test_3():
    assert all_prefixes('WWW') == ['W', 'WW', 'WWW']