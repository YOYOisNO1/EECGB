from program472 import driver
def test0():
  assert driver([1, 2, 3, 4, 5], True) == "PASSED"

def test1():
  assert driver([1, 2, 3, 5, 6], False) == "PASSED"

def test2():
  assert driver([1, 2, 1], False) == "PASSED"

