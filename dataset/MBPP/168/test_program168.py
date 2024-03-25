from program168 import driver
def test0():
  assert driver([1, 2, 3], 4, 0) == "PASSED"

def test1():
  assert driver([1, 2, 2, 3, 3, 3, 4], 3, 3) == "PASSED"

def test2():
  assert driver([0, 1, 2, 3, 1, 2], 1, 2) == "PASSED"

