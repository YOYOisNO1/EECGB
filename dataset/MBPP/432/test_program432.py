from program432 import driver
def test0():
  assert driver(15, 25, 35, 20.0) == "PASSED"

def test1():
  assert driver(10, 20, 30, 15.0) == "PASSED"

def test2():
  assert driver(6, 9, 4, 7.5) == "PASSED"

