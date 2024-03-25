from program53 import driver
def test0():
  assert driver("abcda", "Equal") == "PASSED"

def test1():
  assert driver("ab", "Not Equal") == "PASSED"

def test2():
  assert driver("mad", "Not Equal") == "PASSED"

