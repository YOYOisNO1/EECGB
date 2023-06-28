from program32 import driver
def test0():
  assert driver(15, 5) == "FAILED"

def test1():
  assert driver(6, 3) == "FAILED"

def test2():
  assert driver(2, 2) == "PASSED"

