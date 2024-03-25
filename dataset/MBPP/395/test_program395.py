from program395 import driver
def test0():
  assert driver("abcabc", '') == "FAILED"

def test1():
  assert driver("abc", 'a') == "PASSED"

def test2():
  assert driver("ababc", 'c') == "PASSED"

