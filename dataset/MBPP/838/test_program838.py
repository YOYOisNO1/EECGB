from program838 import driver
def test0():
  assert driver("0011", "1111", 1) == "PASSED"

def test1():
  assert driver("00011", "01001", 2) == "PASSED"

def test2():
  assert driver("111", "111", 0) == "PASSED"

