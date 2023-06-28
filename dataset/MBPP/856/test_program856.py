from program856 import driver
def test0():
  assert driver([1, 0, 1, 0], 4, 3) == "PASSED"

def test1():
  assert driver([0, 1, 0], 3, 1) == "PASSED"

def test2():
  assert driver([0, 0, 1, 1, 0], 5, 2) == "PASSED"

