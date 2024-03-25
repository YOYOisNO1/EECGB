from program897 import driver
def test0():
  assert driver("machine learning", "machine", True) == "PASSED"

def test1():
  assert driver("easy", "fun", False) == "PASSED"

def test2():
  assert driver("python language", "code", False) == "PASSED"

