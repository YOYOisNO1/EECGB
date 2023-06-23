import sys
sys.path.append('../')
from program_124 import valid_date
def test_1():
    assert valid_date('03-11-2000') == True
def test_2():
    assert valid_date('15-01-2012') == False
def test_3():
    assert valid_date('04-0-2040') == False
def test_4():
    assert valid_date('06-04-2020') == True
def test_5():
    assert valid_date('01-01-2007') == True
def test_6():
    assert valid_date('03-32-2011') == False
def test_7():
    assert valid_date('') == False
def test_8():
    assert valid_date('04-31-3000') == False
def test_9():
    assert valid_date('06-06-2005') == True
def test_10():
    assert valid_date('21-31-2000') == False
def test_11():
    assert valid_date('04-12-2003') == True
def test_12():
    assert valid_date('04122003') == False
def test_13():
    assert valid_date('20030412') == False
def test_14():
    assert valid_date('2003-04') == False
def test_15():
    assert valid_date('2003-04-12') == False
def test_16():
    assert valid_date('04-2003') == False