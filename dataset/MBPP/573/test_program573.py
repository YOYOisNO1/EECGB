from program573 import driver
def test0():
  assert driver([10, 20, 30, 40, 20, 50, 60, 40], 720000000) == "PASSED"

def test1():
  assert driver([1, 2, 3, 1], 6) == "PASSED"

def test2():
  assert driver([7, 8, 9, 0, 1, 1], 0) == "PASSED"

