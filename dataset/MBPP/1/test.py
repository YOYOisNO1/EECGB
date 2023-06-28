from program1 import driver
def test0():
  assert driver([[1, 2, 3], [4, 8, 2], [1, 5, 3]], 2, 2, 8) == "PASSED"

def test1():
  assert driver([[2, 3, 4], [5, 9, 3], [2, 6, 4]], 2, 2, 12) == "PASSED"

def test2():
  assert driver([[3, 4, 5], [6, 10, 4], [3, 7, 5]], 2, 2, 16) == "PASSED"

