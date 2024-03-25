from program449 import driver
def test0():
  assert driver(1, 5, 2, 5, 4, 6, "Yes") == "PASSED"

def test1():
  assert driver(1, 1, 1, 4, 1, 5, "No") == "PASSED"

def test2():
  assert driver(1, 1, 1, 1, 1, 1, "No") == "PASSED"

