from program827 import driver
def test0():
  assert driver([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]], 0, 12) == "PASSED"

def test1():
  assert driver([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]], 1, 15) == "PASSED"

def test2():
  assert driver([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]], 3, 9) == "PASSED"

