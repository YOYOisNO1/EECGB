from program715 import driver
def test0():
  assert driver("1, -5, 4, 6, 7", [1, -5, 4, 6, 7]) == "FAILED"

def test1():
  assert driver("1, 2, 3, 4, 5", [1, 2, 3, 4, 5]) == "FAILED"

def test2():
  assert driver("4, 6, 9, 11, 13, 14", [4, 6, 9, 11, 13, 14]) == "FAILED"

