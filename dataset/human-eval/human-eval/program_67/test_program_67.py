import sys
sys.path.append('../')
from program_67 import fruit_distribution
def test_1():
    assert fruit_distribution("5 apples and 6 oranges",19) == 8
def test_2():
    assert fruit_distribution("5 apples and 6 oranges",21) == 10
def test_3():
    assert fruit_distribution("0 apples and 1 oranges",3) == 2
def test_4():
    assert fruit_distribution("1 apples and 0 oranges",3) == 2
def test_5():
    assert fruit_distribution("2 apples and 3 oranges",100) == 95
def test_6():
    assert fruit_distribution("2 apples and 3 oranges",5) == 0
def test_7():
    assert fruit_distribution("1 apples and 100 oranges",120) == 19