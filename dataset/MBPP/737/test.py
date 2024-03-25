from program737 import driver
def test0():
  assert driver("annie", "Valid") == "PASSED"

def test1():
  assert driver("dawood", "Invalid") == "PASSED"

def test2():
  assert driver("Else", "Valid") == "PASSED"

