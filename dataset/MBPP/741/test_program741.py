from program741 import driver
def test0():
  assert driver("python", False) == "PASSED"

def test1():
  assert driver("aaa", True) == "PASSED"

def test2():
  assert driver("data", False) == "PASSED"

