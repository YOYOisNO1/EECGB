from program602 import driver
def test0():
  assert driver("abcabc", "a") == "PASSED"

def test1():
  assert driver("abc", "None") == "PASSED"

def test2():
  assert driver("123123", "1") == "PASSED"

