from program396 import driver
def test0():
  assert driver("abba", "Valid") == "PASSED"

def test1():
  assert driver("a", "Valid") == "PASSED"

def test2():
  assert driver("abcd", "Invalid") == "PASSED"

