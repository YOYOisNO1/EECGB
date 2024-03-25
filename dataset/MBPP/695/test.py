from program695 import driver
def test0():
  assert driver([10, 4, 5], [13, 5, 18], True) == "PASSED"

def test1():
  assert driver([1, 2, 3], [2, 1, 4], False) == "PASSED"

def test2():
  assert driver([4, 5, 6], [5, 6, 7], True) == "PASSED"

