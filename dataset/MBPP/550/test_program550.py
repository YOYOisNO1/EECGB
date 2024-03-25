from program550 import driver
def test0():
  assert driver([2, 3, 5, 6, 9], 0, 4, 9) == "PASSED"

def test1():
  assert driver([3, 4, 5, 2, 1], 0, 4, 5) == "PASSED"

def test2():
  assert driver([1, 2, 3], 0, 2, 3) == "PASSED"

