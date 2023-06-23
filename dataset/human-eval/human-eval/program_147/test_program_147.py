import sys
sys.path.append('../')
from program_147 import get_max_triples
def test_1():
    assert get_max_triples(5) == 1
def test_2():
    assert get_max_triples(6) == 4
def test_3():
    assert get_max_triples(10) == 36
def test_4():
    assert get_max_triples(100) == 53361