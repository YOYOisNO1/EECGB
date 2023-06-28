from program366 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6], 30) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5], 20) == "PASSED"

def test2():
  assert driver([2, 3], 6) == "PASSED"

