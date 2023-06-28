from program359 import driver
def test0():
  assert driver(1, 3, 2, "Yes") == "PASSED"

def test1():
  assert driver(1, 2, 3, "No") == "PASSED"

def test2():
  assert driver(1, -5, 6, "No") == "PASSED"

