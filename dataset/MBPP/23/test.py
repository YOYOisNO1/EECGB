from program23 import driver
def test0():
  assert driver([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]], 33) == "PASSED"

def test1():
  assert driver([[0, 1, 1], [1, 1, 2], [3, 2, 1]], 6) == "PASSED"

def test2():
  assert driver([[0, 1, 3], [1, 2, 1], [9, 8, 2], [0, 1, 0], [6, 4, 8]], 19) == "PASSED"

