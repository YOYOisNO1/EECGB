from program689 import driver
def test0():
  assert driver([1, 3, 6, 1, 0, 9], 6, 3) == "PASSED"

def test1():
  assert driver([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11, 3) == "PASSED"

def test2():
  assert driver([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11, 10) == "PASSED"

