from program917 import driver
def test0():
  assert driver("AaBbGg", "Found a match!") == "PASSED"

def test1():
  assert driver("aA", "Not matched!") == "PASSED"

def test2():
  assert driver("PYTHON", "Not matched!") == "PASSED"

