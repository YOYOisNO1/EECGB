from program281 import driver
def test0():
  assert driver([1, 2, 3], True) == "PASSED"

def test1():
  assert driver([1, 2, 1, 2], False) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 5], True) == "PASSED"

