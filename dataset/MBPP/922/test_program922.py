from program922 import driver
def test0():
  assert driver([1, 2, 3, 4, 7, 0, 8, 4], [7, 8]) == "FAILED"

def test1():
  assert driver([0, -1, -2, -4, 5, 0, -6], [-4, -6]) == "FAILED"

def test2():
  assert driver([1, 3, 5, 6, 8, 9], [8, 9]) == "FAILED"

