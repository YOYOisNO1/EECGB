from program487 import driver
def test0():
  assert driver([[1, 3], [3, 2], [2, 1]], [[2, 1], [3, 2], [1, 3]]) == "PASSED"

def test1():
  assert driver([[2, 4], [3, 3], [1, 1]], [[1, 1], [3, 3], [2, 4]]) == "PASSED"

def test2():
  assert driver([[3, 9], [6, 7], [4, 3]], [[4, 3], [6, 7], [3, 9]]) == "PASSED"

