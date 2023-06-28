from program937 import driver
def test0():
  assert driver("hello world", 'l') == "PASSED"

def test1():
  assert driver("hello ", 'l') == "PASSED"

def test2():
  assert driver("python pr", 'p') == "PASSED"

