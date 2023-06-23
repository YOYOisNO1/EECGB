import sys
sys.path.append('../')
from program_158 import find_max
def test_1():
    assert (find_max(["name", "of", "string"]) == "string"), "t1"
def test_2():
    assert (find_max(["name", "enam", "game"]) == "enam"), 't2'
def test_3():
    assert (find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"), 't3'
def test_4():
    assert (find_max(["abc", "cba"]) == "abc"), 't4'
def test_5():
    assert (find_max(["play", "this", "game", "of","footbott"]) == "footbott"), 't5'
def test_6():
    assert (find_max(["we", "are", "gonna", "rock"]) == "gonna"), 't6'
def test_7():
    assert (find_max(["we", "are", "a", "mad", "nation"]) == "nation"), 't7'
def test_8():
    assert (find_max(["this", "is", "a", "prrk"]) == "this"), 't8'
def test_9():
    assert (find_max(["b"]) == "b"), 't9'
def test_10():
    assert (find_max(["play", "play", "play"]) == "play"), 't10'