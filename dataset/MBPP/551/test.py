from program551 import driver
def test0():
  assert driver([[1, 2, 3], [2, 4, 5], [1, 1, 1]], 0, [1, 2, 1]) == "PASSED"

def test1():
  assert driver([[1, 2, 3], [-2, 4, -5], [1, -1, 1]], 2, [3, -5, 1]) == "PASSED"

def test2():
  assert driver([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]], 0, [1, 5, 1, 13, 5, 9]) == "PASSED"

