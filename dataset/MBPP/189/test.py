from program189 import driver
def test0():
  assert driver([1, 2, 3, -1, 5], 5, 4) == "PASSED"

def test1():
  assert driver([0, -1, -2, 1, 5, 8], 6, 2) == "PASSED"

def test2():
  assert driver([0, 1, 2, 5, -8], 5, 3) == "PASSED"

