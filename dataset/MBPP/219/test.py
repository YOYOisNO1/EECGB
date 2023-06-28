from program219 import driver
def test0():
  assert driver([5, 20, 3, 7, 6, 8], 2, [3, 5, 8, 20]) == "FAILED"

def test1():
  assert driver([4, 5, 6, 1, 2, 7], 3, [1, 2, 4, 5, 6, 7]) == "FAILED"

def test2():
  assert driver([2, 3, 4, 8, 9, 11, 7], 4, [2, 3, 4, 7, 8, 9, 11]) == "FAILED"

