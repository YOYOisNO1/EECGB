from program77 import driver
def test0():
  assert driver(12345, False) == "PASSED"

def test1():
  assert driver(1212112, True) == "PASSED"

def test2():
  assert driver(1212, False) == "PASSED"

