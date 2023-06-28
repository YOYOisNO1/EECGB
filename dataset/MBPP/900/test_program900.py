from program900 import driver
def test0():
  assert driver("5-2345861", True) == "PASSED"

def test1():
  assert driver("6-2345861", False) == "PASSED"

def test2():
  assert driver("78910", False) == "PASSED"

