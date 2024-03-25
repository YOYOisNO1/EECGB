from program61 import driver
def test0():
  assert driver("112112", 6, 6) == "PASSED"

def test1():
  assert driver("111", 3, 6) == "PASSED"

def test2():
  assert driver("1101112", 7, 12) == "PASSED"

