import sys
sys.path.append('../')
from program_15 import string_sequence
def test_1():
    assert string_sequence(0) == '0'
def test_2():
    assert string_sequence(3) == '0 1 2 3'
def test_3():
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'