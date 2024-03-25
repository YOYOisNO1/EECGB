from program505 import driver
def test0():
  assert driver([6, 0, 8, 2, 3, 0, 4, 0, 1], [6, 8, 2, 3, 4, 1, 0, 0, 0]) == "PASSED"

def test1():
  assert driver([4, 0, 2, 7, 0, 9, 0, 12, 0], [4, 2, 7, 9, 12, 0, 0, 0, 0]) == "PASSED"

def test2():
  assert driver([3, 11, 0, 74, 14, 0, 1, 0, 2], [3, 11, 74, 14, 1, 2, 0, 0, 0]) == "PASSED"

