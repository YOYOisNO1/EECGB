import sys
sys.path.append('../')
from program_110 import exchange
def test_1():
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
def test_2():
    assert exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
def test_3():
    assert exchange([1, 2, 3, 4], [2, 1, 4, 3]) == "YES" 
def test_4():
    assert exchange([5, 7, 3], [2, 6, 4]) == "YES"
def test_5():
    assert exchange([5, 7, 3], [2, 6, 3]) == "NO" 
def test_6():
    assert exchange([3, 2, 6, 1, 8, 9], [3, 5, 5, 1, 1, 1]) == "NO"
def test_7():
    assert exchange([100, 200], [200, 200]) == "YES"