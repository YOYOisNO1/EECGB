import sys
sys.path.append('../')
from program_89 import encrypt
def test_1():
    assert encrypt('hi') == 'lm', "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert encrypt('asdfghjkl') == 'ewhjklnop', "This prints if this assert fails 1 (good for debugging!)"
def test_3():
    assert encrypt('gf') == 'kj', "This prints if this assert fails 1 (good for debugging!)"
def test_4():
    assert encrypt('et') == 'ix', "This prints if this assert fails 1 (good for debugging!)"
def test_5():
    assert encrypt('faewfawefaewg')=='jeiajeaijeiak', "This prints if this assert fails 1 (good for debugging!)"
def test_6():
    assert encrypt('hellomyfriend')=='lippsqcjvmirh', "This prints if this assert fails 2 (good for debugging!)"
def test_7():
    assert encrypt('dxzdlmnilfuhmilufhlihufnmlimnufhlimnufhfucufh')=='hbdhpqrmpjylqmpyjlpmlyjrqpmqryjlpmqryjljygyjl', "This prints if this assert fails 3 (good for debugging!)"
def test_8():
    assert encrypt('a')=='e', "This prints if this assert fails 2 (also good for debugging!)"