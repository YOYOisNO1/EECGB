import sys
sys.path.append('../')
from program_148 import bf
def test_1():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus"), "First test error: " + str(len(bf("Jupiter", "Neptune")))      
def test_2():
    assert bf("Earth", "Mercury") == ("Venus",), "Second test error: " + str(bf("Earth", "Mercury"))  
def test_3():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"), "Third test error: " + str(bf("Mercury", "Uranus"))      
def test_4():
    assert bf("Neptune", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus"), "Fourth test error: " + str(bf("Neptune", "Venus"))  
def test_5():
    assert bf("Earth", "Earth") == ()
def test_6():
    assert bf("Mars", "Earth") == ()
def test_7():
    assert bf("Jupiter", "Makemake") == ()