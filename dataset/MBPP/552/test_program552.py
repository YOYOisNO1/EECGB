from program552 import driver
def test0():
  assert driver([0, 2, 4, 6, 8, 10], "Linear Sequence") == "PASSED"

def test1():
  assert driver([1, 2, 3], "Linear Sequence") == "PASSED"

def test2():
  assert driver([1, 5, 2], "Non Linear Sequence") == "PASSED"

