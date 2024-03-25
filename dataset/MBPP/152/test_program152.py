from program152 import driver
def test0():
  assert driver([3, 4, 2, 6, 5, 7, 1, 9], [1, 2, 3, 4, 5, 6, 7, 9]) == "FAILED"

def test1():
  assert driver([7, 25, 45, 78, 11, 33, 19], [7, 11, 19, 25, 33, 45, 78]) == "FAILED"

def test2():
  assert driver([3, 1, 4, 9, 8], [1, 3, 4, 8, 9]) == "FAILED"

