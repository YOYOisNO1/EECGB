from program494 import driver
def test0():
  assert driver([1, 1, 0, 1, 0, 0, 1], "105") == "PASSED"

def test1():
  assert driver([0, 1, 1, 0, 0, 1, 0, 1], "101") == "PASSED"

def test2():
  assert driver([1, 1, 0, 1, 0, 1], "53") == "PASSED"

