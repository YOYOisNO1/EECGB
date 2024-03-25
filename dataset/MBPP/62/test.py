from program62 import driver
def test0():
  assert driver([10, 20, 1, 45, 99], 1) == "PASSED"

def test1():
  assert driver([1, 2, 3], 1) == "PASSED"

def test2():
  assert driver([45, 46, 50, 60], 45) == "PASSED"

