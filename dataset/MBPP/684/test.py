from program684 import driver
def test0():
  assert driver("abcac", 'a', 4) == "PASSED"

def test1():
  assert driver("abca", 'c', 2) == "PASSED"

def test2():
  assert driver("aba", 'a', 7) == "PASSED"

