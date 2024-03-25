from program658 import driver
def test0():
  assert driver([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2], 2) == "PASSED"

def test1():
  assert driver([1, 3, 5, 7, 1, 3, 13, 15, 17, 5, 7, 9, 1, 11], 1) == "PASSED"

def test2():
  assert driver([1, 2, 3, 2, 4, 5, 1, 1, 1], 1) == "PASSED"

