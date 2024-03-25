from program761 import driver
def test0():
  assert driver(9, 45, 3.5357142857142856) == "PASSED"

def test1():
  assert driver(9, 480, None) == "FAILED"

def test2():
  assert driver(5, 270, 11.785714285714285) == "PASSED"

