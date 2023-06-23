import sys
sys.path.append('../')
from program_93 import encode
def test_1():
    assert encode('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert encode('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
def test_3():
    assert encode('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"
def test_4():
    assert encode('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
def test_5():
    assert encode("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"