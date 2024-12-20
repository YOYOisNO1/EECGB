import sys
sys.path.append('../')
from program_7 import filter_by_substring
def test_1():
    assert filter_by_substring([], 'john') == []
def test_2():
    assert filter_by_substring(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']
def test_3():
    assert filter_by_substring(['xxx', 'asd', 'aaaxxy', 'john doe', 'xxxAAA', 'xxx'], 'xx') == ['xxx', 'aaaxxy', 'xxxAAA', 'xxx']
def test_4():
    assert filter_by_substring(['grunt', 'trumpet', 'prune', 'gruesome'], 'run') == ['grunt', 'prune']