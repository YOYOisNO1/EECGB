from program723 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9], 4) == "PASSED"

def test1():
  assert driver([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8], [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8], 11) == "PASSED"

def test2():
  assert driver([2, 4, -6, -9, 11, -12, 14, -5, 17], [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8], 1) == "PASSED"

