import sys
sys.path.append('../')
from program_11 import string_xor
def test_1():
    assert string_xor('111000', '101010') == '010010'
def test_2():
    assert string_xor('1', '1') == '0'
def test_3():
    assert string_xor('0101', '0000') == '0101'