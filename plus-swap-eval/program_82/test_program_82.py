import sys
sys.path.append('../')
from program_82 import prime_length
def test_1():
    assert prime_length('Hello') == True
def test_2():
    assert prime_length('abcdcba') == True
def test_3():
    assert prime_length('kittens') == True
def test_4():
    assert prime_length('orange') == False
def test_5():
    assert prime_length('wow') == True
def test_6():
    assert prime_length('world') == True
def test_7():
    assert prime_length('MadaM') == True
def test_8():
    assert prime_length('Wow') == True
def test_9():
    assert prime_length('') == False
def test_10():
    assert prime_length('HI') == True
def test_11():
    assert prime_length('go') == True
def test_12():
    assert prime_length('gogo') == False
def test_13():
    assert prime_length('aaaaaaaaaaaaaaa') == False
def test_14():
    assert prime_length('Madam') == True
def test_15():
    assert prime_length('M') == False
def test_16():
    assert prime_length('0') == False