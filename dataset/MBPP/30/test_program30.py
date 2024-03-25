from program30 import driver
def test0():
  assert driver("abc", 3) == "FAILED"

def test1():
  assert driver("abcda", 6) == "FAILED"

def test2():
  assert driver("ab", 2) == "FAILED"

