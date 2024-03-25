from program746 import driver
def test0():
  assert driver(4, 45, 6.285714285714286) == "PASSED"

def test1():
  assert driver(9, 45, 31.82142857142857) == "PASSED"

def test2():
  assert driver(9, 360, None) == "FAILED"

