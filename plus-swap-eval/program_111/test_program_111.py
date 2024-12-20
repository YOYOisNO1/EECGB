import sys
sys.path.append('../')
from program_111 import histogram
def test_1():
    assert histogram('a b b a') == {'a':2,'b': 2}, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert histogram('a b c a b') == {'a': 2, 'b': 2}, "This prints if this assert fails 2 (good for debugging!)"
def test_3():
    assert histogram('a b c d g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'g': 1}, "This prints if this assert fails 3 (good for debugging!)"
def test_4():
    assert histogram('r t g') == {'r': 1,'t': 1,'g': 1}, "This prints if this assert fails 4 (good for debugging!)"
def test_5():
    assert histogram('b b b b a') == {'b': 4}, "This prints if this assert fails 5 (good for debugging!)"
def test_6():
    assert histogram('r t g') == {'r': 1,'t': 1,'g': 1}, "This prints if this assert fails 6 (good for debugging!)"
def test_7():
    assert histogram('') == {}, "This prints if this assert fails 7 (also good for debugging!)"
def test_8():
    assert histogram('a') == {'a': 1}, "This prints if this assert fails 8 (also good for debugging!)"