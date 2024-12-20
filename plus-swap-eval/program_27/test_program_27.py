import sys
sys.path.append('../')
from program_27 import flip_case
def test_1():
    assert flip_case('') == ''
def test_2():
    assert flip_case('Hello!') == 'hELLO!'
def test_3():
    assert flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'