from program286 import driver
def test0():
  assert driver([10, 20, -30, -1], 4, 3, 30) == "PASSED"

def test1():
  assert driver([-1, 10, 20], 3, 2, 59) == "PASSED"

def test2():
  assert driver([-1, -2, -3], 3, 3, -1) == "PASSED"

