from program192 import driver
def test0():
  assert driver("thishasboth29", True) == "PASSED"

def test1():
  assert driver("python", False) == "PASSED"

def test2():
  assert driver("string", False) == "PASSED"

