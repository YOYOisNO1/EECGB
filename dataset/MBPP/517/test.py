from program517 import driver
def test0():
  assert driver([1, 2, 3, 4, -1], 4) == "PASSED"

def test1():
  assert driver([0, 1, 2, -5, -1, 6], 6) == "PASSED"

def test2():
  assert driver([0, 0, 1, 0], 1) == "PASSED"

