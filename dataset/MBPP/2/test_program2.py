from program2 import driver
def test0():
  assert driver([3, 4, 5, 6], [5, 7, 4, 10], [4, 5]) == "FAILED"

def test1():
  assert driver([1, 2, 3, 4], [5, 4, 3, 7], [3, 4]) == "FAILED"

def test2():
  assert driver([11, 12, 14, 13], [17, 15, 14, 13], [13, 14]) == "FAILED"

