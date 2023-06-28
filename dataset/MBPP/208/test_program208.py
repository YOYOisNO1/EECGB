from program208 import driver
def test0():
  assert driver("123.11", True) == "PASSED"

def test1():
  assert driver("0.21", True) == "PASSED"

def test2():
  assert driver("123.1214", False) == "PASSED"

