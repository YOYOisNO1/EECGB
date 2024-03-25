from program140 import driver
def test0():
  assert driver([[3, 4, 5], [4, 5, 7], [1, 4]], [3, 4, 5, 7, 1]) == "PASSED"

def test1():
  assert driver([[1, 2, 3], [4, 2, 3], [7, 8]], [1, 2, 3, 4, 7, 8]) == "PASSED"

def test2():
  assert driver([[7, 8, 9], [10, 11, 12], [10, 11]], [7, 8, 9, 10, 11, 12]) == "PASSED"

