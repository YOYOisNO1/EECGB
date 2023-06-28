from program371 import driver
def test0():
  assert driver([0, 1, 2, 3, 4, 5, 6], 0, 6, 7) == "PASSED"

def test1():
  assert driver([0, 1, 2, 6, 9, 11, 15], 0, 6, 3) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 6, 9, 11, 15], 0, 7, 0) == "PASSED"

