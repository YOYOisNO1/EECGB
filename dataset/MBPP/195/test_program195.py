from program195 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6, 6], 6, 6, 5) == "PASSED"

def test1():
  assert driver([1, 2, 2, 2, 3, 2, 2, 4, 2], 2, 9, 1) == "PASSED"

def test2():
  assert driver([1, 2, 3], 1, 3, 0) == "PASSED"

