from program842 import driver
def test0():
  assert driver([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2], 13, 5) == "PASSED"

def test1():
  assert driver([1, 2, 3, 2, 3, 1, 3], 7, 3) == "PASSED"

def test2():
  assert driver([5, 7, 2, 7, 5, 2, 5], 7, 5) == "PASSED"

