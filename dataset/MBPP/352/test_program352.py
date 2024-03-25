from program352 import driver
def test0():
  assert driver("aba", False) == "PASSED"

def test1():
  assert driver("abc", True) == "PASSED"

def test2():
  assert driver("abab", False) == "PASSED"

