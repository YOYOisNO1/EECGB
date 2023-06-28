from program68 import driver
def test0():
  assert driver([6, 5, 4, 4], True) == "PASSED"

def test1():
  assert driver([1, 2, 2, 3], True) == "PASSED"

def test2():
  assert driver([1, 3, 2], False) == "PASSED"

