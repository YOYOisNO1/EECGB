from program589 import driver
def test0():
  assert driver(1, 30, [1, 4, 9, 16, 25]) == "PASSED"

def test1():
  assert driver(50, 100, [64, 81, 100]) == "PASSED"

def test2():
  assert driver(100, 200, [100, 121, 144, 169, 196]) == "PASSED"

