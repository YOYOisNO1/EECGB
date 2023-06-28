from program587 import driver
def test0():
  assert driver([5, 10, 7, 4, 15, 3], [5, 10, 7, 4, 15, 3]) == "FAILED"

def test1():
  assert driver([2, 4, 5, 6, 2, 3, 4, 4, 7], [2, 4, 5, 6, 2, 3, 4, 4, 7]) == "FAILED"

def test2():
  assert driver([58, 44, 56], [58, 44, 56]) == "FAILED"

