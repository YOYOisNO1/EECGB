from program442 import driver
def test0():
  assert driver([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8], 0.54) == "PASSED"

def test1():
  assert driver([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8], 0.69) == "PASSED"

def test2():
  assert driver([2, 4, -6, -9, 11, -12, 14, -5, 17], 0.56) == "PASSED"

