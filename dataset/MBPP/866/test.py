from program866 import driver
def test0():
  assert driver("February", False) == "PASSED"

def test1():
  assert driver("January", True) == "PASSED"

def test2():
  assert driver("March", True) == "PASSED"

