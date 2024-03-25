from program792 import driver
def test0():
  assert driver([[1, 3], [5, 7], [9, 11], [13, 15, 17]], 4) == "PASSED"

def test1():
  assert driver([[1, 2], [2, 3], [4, 5]], 3) == "PASSED"

def test2():
  assert driver([[1, 0], [2, 0]], 2) == "PASSED"

