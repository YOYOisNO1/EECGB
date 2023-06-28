from program323 import driver
def test0():
  assert driver([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8], 10, [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]) == "FAILED"

def test1():
  assert driver([1, 2, 3, -4, -1, 4], 6, [-4, 1, -1, 2, 3, 4]) == "FAILED"

def test2():
  assert driver([4, 7, 9, 77, -4, 5, -3, -9], 8, [-4, 4, -3, 7, -9, 9, 77, 5]) == "FAILED"

