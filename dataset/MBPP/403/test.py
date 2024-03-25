from program403 import driver
def test0():
  assert driver("https://www.google.com", True) == "PASSED"

def test1():
  assert driver("https:/www.gmail.com", False) == "PASSED"

def test2():
  assert driver("https:// www.redit.com", False) == "PASSED"

