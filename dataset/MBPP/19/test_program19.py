from program19 import driver
def test0():
  assert driver([1, 2, 3, 4, 5], False) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 4], True) == "PASSED"

def test2():
  assert driver([1, 1, 2, 2, 3, 3, 4, 4, 5], True) == "PASSED"

