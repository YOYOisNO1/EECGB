from program819 import driver
def test0():
  assert driver([1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5], [[1, 2, 4, 5], [1, 3, 3, 4]]) == "FAILED"

def test1():
  assert driver([2, 2, 3, 1, 2, 6, 7, 9], [[2, 3, 1, 2, 6, 7, 9], [2, 1, 1, 1, 1, 1, 1]]) == "FAILED"

def test2():
  assert driver([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], [[2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == "FAILED"

