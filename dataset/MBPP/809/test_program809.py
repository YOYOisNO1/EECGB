from program809 import driver
def test0():
  assert driver([1, 2, 3], [2, 3, 4], False) == "PASSED"

def test1():
  assert driver([4, 5, 6], [3, 4, 5], True) == "PASSED"

def test2():
  assert driver([11, 12, 13], [10, 11, 12], True) == "PASSED"

