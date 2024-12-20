import sys
sys.path.append('../')
from program_161 import solve
def test_1():
    assert solve("AsDf") == "aSdF"
def test_2():
    assert solve("1234") == "4321"
def test_3():
    assert solve("ab") == "AB"
def test_4():
    assert solve("#a@C") == "#A@c"
def test_5():
    assert solve("#AsdfW^45") == "#aSDFw^45"
def test_6():
    assert solve("#6@2") == "2@6#"
def test_7():
    assert solve("#$a^D") == "#$A^d"
def test_8():
    assert solve("#ccc") == "#CCC"