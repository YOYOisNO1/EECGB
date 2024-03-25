from program871 import driver
def test0():
  assert driver("abc", "cba", False) == "PASSED"

def test1():
  assert driver("abcd", "cdba", False) == "PASSED"

def test2():
  assert driver("abacd", "cdaba", True) == "PASSED"

