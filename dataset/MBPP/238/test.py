from program238 import driver
def test0():
  assert driver("abc", 6) == "PASSED"

def test1():
  assert driver("abcd", 10) == "PASSED"

def test2():
  assert driver("abcde", 15) == "PASSED"

