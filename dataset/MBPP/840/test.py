from program840 import driver
def test0():
  assert driver(2, 0, -1, "Yes") == "PASSED"

def test1():
  assert driver(1, -5, 6, "No") == "PASSED"

def test2():
  assert driver(2, 0, 2, "Yes") == "PASSED"

