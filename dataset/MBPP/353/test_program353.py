from program353 import driver
def test0():
  assert driver([[1, 2, 3], [2, 4, 5], [1, 1, 1]], 0, [[2, 3], [4, 5], [1, 1]]) == "PASSED"

def test1():
  assert driver([[1, 2, 3], [-2, 4, -5], [1, -1, 1]], 2, [[1, 2], [-2, 4], [1, -1]]) == "PASSED"

def test2():
  assert driver([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]], 0, [[3], [7], [3], [15, 17], [7], [11]]) == "PASSED"

