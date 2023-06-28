from program967 import driver
def test0():
  assert driver("SEEquoiaL", "accepted") == "PASSED"

def test1():
  assert driver("program", "not accepted") == "PASSED"

def test2():
  assert driver("fine", "not accepted") == "PASSED"

