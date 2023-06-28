from program802 import driver
def test0():
  assert driver([3, 2, 1], 3, 1) == "PASSED"

def test1():
  assert driver([4, 5, 1, 2, 3], 5, 2) == "PASSED"

def test2():
  assert driver([7, 8, 9, 1, 2, 3], 6, 3) == "PASSED"

