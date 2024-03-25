from program651 import driver
def test0():
  assert driver([10, 4, 5, 6], [5, 10], True) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4], [5, 6], False) == "PASSED"

def test2():
  assert driver([7, 8, 9, 10], [10, 8], True) == "PASSED"

