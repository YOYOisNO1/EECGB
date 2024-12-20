import sys
sys.path.append('../')
from program_16 import count_distinct_characters
def test_1():
    assert count_distinct_characters('') == 0
def test_2():
    assert count_distinct_characters('abcde') == 5
def test_3():
    assert count_distinct_characters('abcde' + 'cade' + 'CADE') == 5
def test_4():
    assert count_distinct_characters('aaaaAAAAaaaa') == 1
def test_5():
    assert count_distinct_characters('Jerry jERRY JeRRRY') == 5