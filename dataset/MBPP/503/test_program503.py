from program503 import driver
def test0():
  assert driver([1, 1, 3, 4, 4, 5, 6, 7], [2, 4, 7, 8, 9, 11, 13]) == "PASSED"

def test1():
  assert driver([4, 5, 8, 9, 6, 10], [9, 13, 17, 15, 16]) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 5, 7, 9, 11, 13, 15, 17, 19]) == "PASSED"

