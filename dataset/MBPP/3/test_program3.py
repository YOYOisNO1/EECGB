from program3 import driver
def test0():
  assert driver(2, False) == "PASSED"

def test1():
  assert driver(10, True) == "PASSED"

def test2():
  assert driver(35, True) == "PASSED"

