from program743 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 4, [8, 9, 10, 1, 2, 3, 4, 5, 6]) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 2, [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 2, [6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8]) == "PASSED"

