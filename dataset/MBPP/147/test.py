from program147 import driver
def test0():
  assert driver([[1, 0, 0], [4, 8, 0], [1, 5, 3]], 2, 2, 14) == "PASSED"

def test1():
  assert driver([[13, 0, 0], [7, 4, 0], [2, 4, 6]], 2, 2, 24) == "PASSED"

def test2():
  assert driver([[2, 0, 0], [11, 18, 0], [21, 25, 33]], 2, 2, 53) == "PASSED"

