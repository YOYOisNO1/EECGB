from program92 import driver
def test0():
  assert driver("1212121", True) == "PASSED"

def test1():
  assert driver("1991", False) == "PASSED"

def test2():
  assert driver("121", True) == "PASSED"

