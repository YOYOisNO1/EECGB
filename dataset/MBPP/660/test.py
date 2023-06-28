from program660 import driver
def test0():
  assert driver(5, 10, 1, 5, [1, 10]) == "FAILED"

def test1():
  assert driver(3, 5, 7, 9, [3, 9]) == "FAILED"

def test2():
  assert driver(1, 5, 2, 8, [1, 8]) == "FAILED"

