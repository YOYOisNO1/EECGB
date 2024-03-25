from program541 import driver
def test0():
  assert driver(12, True) == "FAILED"

def test1():
  assert driver(15, False) == "FAILED"

def test2():
  assert driver(18, True) == "FAILED"

