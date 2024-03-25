from program790 import driver
def test0():
  assert driver([3, 2, 1], False) == "PASSED"

def test1():
  assert driver([1, 2, 3], False) == "PASSED"

def test2():
  assert driver([2, 1, 4], True) == "PASSED"

