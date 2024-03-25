from program452 import driver
def test0():
  assert driver(1500, 1200, None) == "PASSED"

def test1():
  assert driver(100, 200, 100) == "PASSED"

def test2():
  assert driver(2000, 5000, 3000) == "PASSED"

