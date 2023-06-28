from program191 import driver
def test0():
  assert driver("February", False) == "PASSED"

def test1():
  assert driver("June", True) == "PASSED"

def test2():
  assert driver("April", True) == "PASSED"

