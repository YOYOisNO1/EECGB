from program466 import driver
def test0():
  assert driver([1, 3, 20, 4, 1, 0], 6, 2) == "FAILED"

def test1():
  assert driver([2, 3, 4, 5, 6], 5, 4) == "FAILED"

def test2():
  assert driver([8, 9, 11, 12, 14, 15], 6, 5) == "FAILED"

