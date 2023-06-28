from program387 import driver
def test0():
  assert driver("AB3454D", "Odd") == "PASSED"

def test1():
  assert driver("ABC", "Even") == "PASSED"

def test2():
  assert driver("AAD", "Odd") == "PASSED"

