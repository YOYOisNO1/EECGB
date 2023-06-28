from program636 import driver
def test0():
  assert driver(2, 0, 2, "Yes") == "PASSED"

def test1():
  assert driver(2, -5, 2, "Yes") == "PASSED"

def test2():
  assert driver(1, 2, 3, "No") == "PASSED"

