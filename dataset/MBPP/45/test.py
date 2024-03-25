from program45 import driver
def test0():
  assert driver([2, 4, 6, 8, 16], 2) == "FAILED"

def test1():
  assert driver([1, 2, 3], 1) == "FAILED"

def test2():
  assert driver([2, 4, 6, 8], 2) == "FAILED"

