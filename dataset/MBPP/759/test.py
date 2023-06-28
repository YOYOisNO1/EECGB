from program759 import driver
def test0():
  assert driver("123.11", True) == "PASSED"

def test1():
  assert driver("e666.86", False) == "PASSED"

def test2():
  assert driver("3.124587", False) == "PASSED"

