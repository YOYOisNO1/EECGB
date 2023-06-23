import sys
sys.path.append('../')
from program_56 import correct_bracketing
def test_1():
    assert correct_bracketing("<>")
def test_2():
    assert correct_bracketing("<<><>>")
def test_3():
    assert correct_bracketing("<><><<><>><>")
def test_4():
    assert correct_bracketing("<><><<<><><>><>><<><><<>>>")
def test_5():
    assert not correct_bracketing("<<<><>>>>")
def test_6():
    assert not correct_bracketing("><<>")
def test_7():
    assert not correct_bracketing("<")
def test_8():
    assert not correct_bracketing("<<<<")
def test_9():
    assert not correct_bracketing(">")
def test_10():
    assert not correct_bracketing("<<>")
def test_11():
    assert not correct_bracketing("<><><<><>><>><<>")
def test_12():
    assert not correct_bracketing("<><><<><>><>>><>")