from program930 import driver
def test0():
  assert driver("msb", "Not matched!") == "PASSED"

def test1():
  assert driver("a0c", "Found a match!") == "PASSED"

def test2():
  assert driver("abbc", "Found a match!") == "PASSED"

