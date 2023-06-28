from program225 import driver
def test0():
  assert driver([1, 2, 3, 4, 5], 0, 4, 1) == "PASSED"

def test1():
  assert driver([4, 6, 8], 0, 2, 4) == "PASSED"

def test2():
  assert driver([2, 3, 5, 7, 9], 0, 4, 2) == "PASSED"

