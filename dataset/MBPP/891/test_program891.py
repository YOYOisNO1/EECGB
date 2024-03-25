from program891 import driver
def test0():
  assert driver(12, 1, False) == "PASSED"

def test1():
  assert driver(2, 2, True) == "PASSED"

def test2():
  assert driver(10, 20, True) == "PASSED"

