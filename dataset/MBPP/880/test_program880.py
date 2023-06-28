from program880 import driver
def test0():
  assert driver(2, 5, 2, "2 solutions") == "PASSED"

def test1():
  assert driver(1, 1, 1, "No solutions") == "PASSED"

def test2():
  assert driver(1, 2, 1, "1 solution") == "PASSED"

