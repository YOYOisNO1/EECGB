from program11 import driver
def test0():
  assert driver("hello", 'l', "heo") == "PASSED"

def test1():
  assert driver("abcda", 'a', "bcd") == "PASSED"

def test2():
  assert driver("PHP", 'P', "H") == "PASSED"

