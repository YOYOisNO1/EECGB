from program386 import driver
def test0():
  assert driver("[]][][", 2) == "PASSED"

def test1():
  assert driver("[[][]]", 0) == "PASSED"

def test2():
  assert driver("[[][]]][", 1) == "PASSED"

