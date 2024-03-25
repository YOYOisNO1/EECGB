from program726 import driver
def test0():
  assert driver([1, 5, 7, 8, 10], [5, 35, 56, 80]) == "FAILED"

def test1():
  assert driver([2, 4, 5, 6, 7], [8, 20, 30, 42]) == "FAILED"

def test2():
  assert driver([12, 13, 14, 9, 15], [156, 182, 126, 135]) == "FAILED"

