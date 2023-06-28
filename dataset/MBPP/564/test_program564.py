from program564 import driver
def test0():
  assert driver([1, 2, 1], 3, 2) == "PASSED"

def test1():
  assert driver([1, 1, 1, 1], 4, 0) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 5], 5, 10) == "PASSED"

