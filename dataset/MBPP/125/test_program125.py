from program125 import driver
def test0():
  assert driver("11000010001", 11, 6) == "PASSED"

def test1():
  assert driver("10111", 5, 1) == "PASSED"

def test2():
  assert driver("11011101100101", 14, 2) == "PASSED"

