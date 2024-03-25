from program630 import driver
def test0():
  assert driver([3, 4], [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]) == "FAILED"

def test1():
  assert driver([4, 5], [[3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6]]) == "FAILED"

def test2():
  assert driver([5, 6], [[4, 5], [4, 6], [4, 7], [5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7]]) == "FAILED"

