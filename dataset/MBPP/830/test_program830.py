from program830 import driver
def test0():
  assert driver(123.01247, 0, 124.0) == "PASSED"

def test1():
  assert driver(123.01247, 1, 123.1) == "PASSED"

def test2():
  assert driver(123.01247, 2, 123.02) == "PASSED"

