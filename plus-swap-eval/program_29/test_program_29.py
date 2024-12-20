import sys
sys.path.append('../')
from program_29 import filter_by_prefix
def test_1():
    assert filter_by_prefix([], 'john') == []
def test_2():
    assert filter_by_prefix(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']