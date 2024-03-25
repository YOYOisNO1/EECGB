from program477 import driver
def test0():
  assert driver("InValid", "invalid") == "PASSED"

def test1():
  assert driver("TruE", "true") == "PASSED"

def test2():
  assert driver("SenTenCE", "sentence") == "PASSED"

