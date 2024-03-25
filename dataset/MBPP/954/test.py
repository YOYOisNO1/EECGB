from program954 import driver
def test0():
  assert driver(1500, 1200, 300) == "PASSED"

def test1():
  assert driver(100, 200, None) == "PASSED"

def test2():
  assert driver(2000, 5000, None) == "PASSED"

