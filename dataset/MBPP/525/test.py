from program525 import driver
def test0():
  assert driver([2, 3, 4], [2, 3, 8], True) == "PASSED"

def test1():
  assert driver([2, 3, 4], [4, -3, 8], False) == "PASSED"

def test2():
  assert driver([3, 3], [5, 5], True) == "PASSED"

