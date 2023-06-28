from program151 import driver
def test0():
  assert driver(17, 13, True) == "PASSED"

def test1():
  assert driver(15, 21, False) == "FAILED"

def test2():
  assert driver(25, 45, False) == "FAILED"

