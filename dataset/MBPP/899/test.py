from program899 import driver
def test0():
  assert driver([3, 2, 1, 2, 3, 4], 6, True) == "PASSED"

def test1():
  assert driver([2, 1, 4, 5, 1], 5, True) == "PASSED"

def test2():
  assert driver([1, 2, 2, 1, 2, 3], 6, True) == "PASSED"

