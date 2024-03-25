from program106 import driver
def test0():
  assert driver([5, 6, 7], [9, 10], [9, 10, 5, 6, 7]) == "FAILED"

def test1():
  assert driver([6, 7, 8], [10, 11], [10, 11, 6, 7, 8]) == "FAILED"

def test2():
  assert driver([7, 8, 9], [11, 12], [11, 12, 7, 8, 9]) == "FAILED"

