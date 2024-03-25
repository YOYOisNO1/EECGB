from program42 import driver
def test0():
  assert driver([1, 2, 3, 1, 1, 4, 5, 6], 8, 3) == "PASSED"

def test1():
  assert driver([1, 2, 3, 1, 1], 5, 3) == "PASSED"

def test2():
  assert driver([1, 1, 2], 3, 2) == "PASSED"

