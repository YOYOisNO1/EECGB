import sys
sys.path.append('../')
from program_98 import count_upper
def test_1():
    assert count_upper('aBCdEf')  == 1
def test_2():
    assert count_upper('abcdefg') == 0
def test_3():
    assert count_upper('dBBE') == 0
def test_4():
    assert count_upper('B')  == 0
def test_5():
    assert count_upper('U')  == 1
def test_6():
    assert count_upper('') == 0
def test_7():
    assert count_upper('EEEE') == 2
def test_8():
    assert True