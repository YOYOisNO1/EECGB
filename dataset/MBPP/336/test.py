from program336 import driver
def test0():
  assert driver("February", True) == "PASSED"

def test1():
  assert driver("January", False) == "PASSED"

def test2():
  assert driver("March", False) == "PASSED"

