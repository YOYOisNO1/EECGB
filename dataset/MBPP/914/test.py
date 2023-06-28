from program914 import driver
def test0():
  assert driver("abab", True) == "PASSED"

def test1():
  assert driver("aaaa", False) == "PASSED"

def test2():
  assert driver("xyz", False) == "PASSED"

