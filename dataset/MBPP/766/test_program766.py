from program766 import driver
def test0():
  assert driver([1, 1, 2, 3, 3, 4, 4, 5], [[1, 1], [1, 2], [2, 3], [3, 3], [3, 4], [4, 4], [4, 5]]) == "FAILED"

def test1():
  assert driver([1, 5, 7, 9, 10], [[1, 5], [5, 7], [7, 9], [9, 10]]) == "FAILED"

def test2():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == "FAILED"

