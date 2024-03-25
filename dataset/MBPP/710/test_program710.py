from program710 import driver
def test0():
  assert driver([10, 4, 5, 6, 7], [10, 7]) == "FAILED"

def test1():
  assert driver([1, 2, 3, 4, 5], [1, 5]) == "FAILED"

def test2():
  assert driver([6, 7, 8, 9, 10], [6, 10]) == "FAILED"

