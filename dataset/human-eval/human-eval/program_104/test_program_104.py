import sys
sys.path.append('../')
from program_104 import unique_digits
def test_1():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
def test_2():
    assert unique_digits([152, 323, 1422, 10]) == []
def test_3():
    assert unique_digits([12345, 2033, 111, 151]) == [111, 151]
def test_4():
    assert unique_digits([135, 103, 31]) == [31, 135]
def test_5():
    assert True