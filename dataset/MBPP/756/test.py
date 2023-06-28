from program756 import driver
def test0():
  assert driver("ac", "Found a match!") == "PASSED"

def test1():
  assert driver("dc", "Not matched!") == "PASSED"

def test2():
  assert driver("abbbba", "Found a match!") == "PASSED"

