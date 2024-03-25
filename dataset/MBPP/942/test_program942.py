from program942 import driver
def test0():
  assert driver([4, 5, 7, 9, 3], [6, 7, 10, 11], True) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4], [4, 6, 7, 8, 9], True) == "PASSED"

def test2():
  assert driver([3, 2, 1, 4, 5], [9, 8, 7, 6], False) == "PASSED"

