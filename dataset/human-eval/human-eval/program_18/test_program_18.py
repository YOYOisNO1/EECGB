import sys
sys.path.append('../')
from program_18 import how_many_times
def test_1():
    assert how_many_times('', 'x') == 0
def test_2():
    assert how_many_times('xyxyxyx', 'x') == 4
def test_3():
    assert how_many_times('cacacacac', 'cac') == 4
def test_4():
    assert how_many_times('john doe', 'john') == 1