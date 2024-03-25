from program721 import driver
def test0():
  assert driver([[1, 2, 3], [6, 5, 4], [7, 3, 9]], 3, 5.2) == "PASSED"

def test1():
  assert driver([[2, 3, 4], [7, 6, 5], [8, 4, 10]], 3, 6.2) == "PASSED"

def test2():
  assert driver([[3, 4, 5], [8, 7, 6], [9, 5, 11]], 3, 7.2) == "PASSED"

