from program56 import driver
def test0():
  assert driver(70, False) == "FAILED"

def test1():
  assert driver(23, False) == "FAILED"

def test2():
  assert driver(73, True) == "FAILED"

