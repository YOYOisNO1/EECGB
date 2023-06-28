from program878 import driver
def test0():
  assert driver([3, 5, 6, 5, 3, 6], [3, 6, 5], True) == "PASSED"

def test1():
  assert driver([4, 5, 6, 4, 6, 5], [4, 5, 6], True) == "PASSED"

def test2():
  assert driver([9, 8, 7, 6, 8, 9], [9, 8, 1], False) == "PASSED"

