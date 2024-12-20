import sys
sys.path.append('../')
from program_112 import reverse_delete
def test_1():
    assert reverse_delete("abcde","ae") == ('bcd',False)
def test_2():
    assert reverse_delete("abcdef", "b") == ('acdef',False)
def test_3():
    assert reverse_delete("abcdedcba","ab") == ('cdedc',True)
def test_4():
    assert reverse_delete("dwik","w") == ('dik',False)
def test_5():
    assert reverse_delete("a","a") == ('',True)
def test_6():
    assert reverse_delete("abcdedcba","") == ('abcdedcba',True)
def test_7():
    assert reverse_delete("abcdedcba","v") == ('abcdedcba',True)
def test_8():
    assert reverse_delete("vabba","v") == ('abba',True)
def test_9():
    assert reverse_delete("mamma", "mia") == ("", True)