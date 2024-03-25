from program362 import driver
def test0():
  assert driver([1, 2, 3, 1, 2, 3, 12, 4, 2], 2) == "PASSED"

def test1():
  assert driver([1, 2, 6, 7, 0, 1, 0, 1, 0], 1) == "PASSED"

def test2():
  assert driver([1, 2, 3, 1, 2, 4, 1], 1) == "PASSED"

