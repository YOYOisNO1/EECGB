from program231 import driver
def test0():
  assert driver([[1], [2, 1], [3, 3, 2]], 3, 6) == "PASSED"

def test1():
  assert driver([[1], [1, 2], [4, 1, 12]], 3, 15) == "PASSED"

def test2():
  assert driver([[2], [3, 2], [13, 23, 12]], 3, 28) == "PASSED"

