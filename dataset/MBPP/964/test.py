from program964 import driver
def test0():
  assert driver("program", False) == "PASSED"

def test1():
  assert driver("solution", True) == "PASSED"

def test2():
  assert driver("data", True) == "PASSED"

