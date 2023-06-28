from program324 import driver
def test0():
  assert driver([5, 6, 3, 6, 10, 34], [46, 18]) == "FAILED"

def test1():
  assert driver([1, 2, 3, 4, 5], [6, 9]) == "FAILED"

def test2():
  assert driver([6, 7, 8, 9, 4, 5], [21, 18]) == "FAILED"

