from program166 import driver
def test0():
  assert driver([5, 4, 7, 2, 1], 5, 4) == "PASSED"

def test1():
  assert driver([7, 2, 8, 1, 0, 5, 11], 7, 9) == "PASSED"

def test2():
  assert driver([1, 2, 3], 3, 1) == "PASSED"

