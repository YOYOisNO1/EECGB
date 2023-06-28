from program130 import driver
def test0():
  assert driver([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2], [2, 5]) == "FAILED"

def test1():
  assert driver([2, 3, 8, 4, 7, 9, 8, 7, 9, 15, 14, 10, 12, 13, 16, 16, 18], [8, 2]) == "FAILED"

def test2():
  assert driver([10, 20, 20, 30, 40, 90, 80, 50, 30, 20, 50, 10], [20, 3]) == "FAILED"

