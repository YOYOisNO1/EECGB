import sys
sys.path.append('../')
from program_86 import anti_shuffle
def test_1():
    assert anti_shuffle('Hi') == 'Hi'
def test_2():
    assert anti_shuffle('hello') == 'ehllo'
def test_3():
    assert anti_shuffle('number') == 'bemnru'
def test_4():
    assert anti_shuffle('abcd') == 'abcd'
def test_5():
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'
def test_6():
    assert anti_shuffle('') == ''
def test_7():
    assert anti_shuffle('Hi. My name is Mister Robot. How are you?') == '.Hi My aemn is Meirst .Rboot How aer ?ouy'
def test_8():
    assert True