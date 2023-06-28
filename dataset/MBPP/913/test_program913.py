from program913 import driver
def test0():
  assert driver("abcdef", False) == "PASSED"

def test1():
  assert driver("abcdef7", True) == "PASSED"

def test2():
  assert driver("abc", False) == "PASSED"

