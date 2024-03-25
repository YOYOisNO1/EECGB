from program25 import driver
def test0():
  assert driver([1, 1, 2, 3], 4, 6) == "PASSED"

def test1():
  assert driver([1, 2, 3, 1, 1], 5, 6) == "PASSED"

def test2():
  assert driver([1, 1, 4, 5, 6], 5, 120) == "PASSED"

