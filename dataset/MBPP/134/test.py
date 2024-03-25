from program134 import driver
def test0():
  assert driver([5, 7, 10], 3, 1, "ODD") == "FAILED"

def test1():
  assert driver([2, 3], 2, 3, "EVEN") == "FAILED"

def test2():
  assert driver([1, 2, 3], 3, 1, "ODD") == "FAILED"

