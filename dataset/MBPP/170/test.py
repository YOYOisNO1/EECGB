from program170 import driver
def test0():
  assert driver([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 8, 10, 29) == "PASSED"

def test1():
  assert driver([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 5, 7, 16) == "PASSED"

def test2():
  assert driver([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 7, 10, 38) == "PASSED"

