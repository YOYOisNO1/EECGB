from program470 import driver
def test0():
  assert driver([1, 5, 7, 8, 10], [6, 12, 15, 18]) == "FAILED"

def test1():
  assert driver([2, 6, 8, 9, 11], [8, 14, 17, 20]) == "FAILED"

def test2():
  assert driver([3, 7, 9, 10, 12], [10, 16, 19, 22]) == "FAILED"

