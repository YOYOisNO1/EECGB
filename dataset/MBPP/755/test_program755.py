from program755 import driver
def test0():
  assert driver([1.0, 2.0, -8.0, -2.0, 0.0, -2.0], -2.0) == "PASSED"

def test1():
  assert driver([1.0, 1.0, -0.5, 0.0, 2.0, -2.0, -2.0], -0.5) == "PASSED"

def test2():
  assert driver([2.0, 2.0], None) == "FAILED"

