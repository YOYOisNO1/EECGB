from program885 import driver
def test0():
  assert driver("paper", "title", True) == "PASSED"

def test1():
  assert driver("ab", "ba", True) == "PASSED"

def test2():
  assert driver("ab", "aa", False) == "PASSED"

