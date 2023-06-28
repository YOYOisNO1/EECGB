from program822 import driver
def test0():
  assert driver("password", False) == "PASSED"

def test1():
  assert driver("Password@10", True) == "PASSED"

def test2():
  assert driver("password@10", False) == "PASSED"

