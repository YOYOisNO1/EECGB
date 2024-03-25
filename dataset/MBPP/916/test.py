from program916 import driver
def test0():
  assert driver([1, 4, 45, 6, 10, 8], 6, 22, [4, 10, 8]) == "FAILED"

def test1():
  assert driver([12, 3, 5, 2, 6, 9], 6, 24, [12, 3, 9]) == "FAILED"

def test2():
  assert driver([1, 2, 3, 4, 5], 5, 9, [1, 3, 5]) == "FAILED"

