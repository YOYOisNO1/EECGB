from program74 import driver
def test0():
  assert driver(["red", "green", "green"], ['a', 'b', 'b'], True) == "PASSED"

def test1():
  assert driver(["red", "green", "greenn"], ['a', 'b', 'b'], False) == "PASSED"

def test2():
  assert driver(["red", "green", "greenn"], ['a', 'b'], False) == "PASSED"

