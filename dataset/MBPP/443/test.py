from program443 import driver
def test0():
  assert driver([1, 2, 3, -4, -6], -6) == "PASSED"

def test1():
  assert driver([1, 2, 3, -8, -9], -9) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, -1], -1) == "PASSED"

