from program12 import driver
def test0():
  assert driver([[1, 2, 3], [2, 4, 5], [1, 1, 1]], [[1, 1, 1], [1, 2, 3], [2, 4, 5]]) == "PASSED"

def test1():
  assert driver([[1, 2, 3], [-2, 4, -5], [1, -1, 1]], [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]) == "PASSED"

def test2():
  assert driver([[5, 8, 9], [6, 4, 3], [2, 1, 4]], [[2, 1, 4], [6, 4, 3], [5, 8, 9]]) == "PASSED"

