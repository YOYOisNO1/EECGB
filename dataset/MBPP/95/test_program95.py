from program95 import driver
def test0():
  assert driver([[1], [1, 2]], 1) == "PASSED"

def test1():
  assert driver([[1, 2], [1, 2, 3], [1, 2, 3, 4]], 2) == "PASSED"

def test2():
  assert driver([[3, 3, 3], [4, 4, 4, 4]], 3) == "PASSED"

