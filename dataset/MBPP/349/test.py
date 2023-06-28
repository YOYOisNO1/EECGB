from program349 import driver
def test0():
  assert driver("01010101010", "Yes") == "PASSED"

def test1():
  assert driver("name0", "No") == "PASSED"

def test2():
  assert driver("101", "Yes") == "PASSED"

