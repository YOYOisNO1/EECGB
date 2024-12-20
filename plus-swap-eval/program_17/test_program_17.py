import sys
sys.path.append('../')
from program_17 import parse_music
def test_1():
    assert parse_music('') == []
def test_2():
    assert parse_music('o o o o') == [4, 4, 4, 4]
def test_3():
    assert parse_music('.| .| .| .|') == [1, 1, 1, 1]
def test_4():
    assert parse_music('o| o| .| .| o o o o') == [2, 2, 1, 1, 4, 4, 4, 4]
def test_5():
    assert parse_music('o| .| o| .| o o| o o|') == [2, 1, 2, 1, 4, 2, 4, 2]