from program767 import driver
def test0():
  assert driver([1, 1, 1, 1], 4, 2, 6) == "PASSED"

def test1():
  assert driver([1, 5, 7, -1, 5], 5, 6, 3) == "PASSED"

def test2():
  assert driver([1, -2, 3], 3, 1, 1) == "PASSED"

