from program649 import driver
def test0():
  assert driver([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 8, 10, 29) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5], 1, 2, 5) == "PASSED"

def test2():
  assert driver([1, 0, 1, 2, 5, 6], 4, 5, 11) == "PASSED"

