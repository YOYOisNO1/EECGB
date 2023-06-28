from program701 import driver
def test0():
  assert driver([1, 2, 3, 4, 1, 2, 3], 3) == "PASSED"

def test1():
  assert driver([-7, 1, 5, 2, -4, 3, 0], 3) == "PASSED"

def test2():
  assert driver([1, 2, 3], -1) == "PASSED"

