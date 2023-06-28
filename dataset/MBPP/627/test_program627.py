from program627 import driver
def test0():
  assert driver([0, 1, 2, 3], 0, 3, 4) == "PASSED"

def test1():
  assert driver([0, 1, 2, 6, 9], 0, 4, 3) == "PASSED"

def test2():
  assert driver([2, 3, 5, 8, 9], 0, 4, 0) == "PASSED"

