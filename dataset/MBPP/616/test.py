from program616 import driver
def test0():
  assert driver([10, 4, 5, 6], [5, 6, 7, 5], [0, 4, 5, 1]) == "FAILED"

def test1():
  assert driver([11, 5, 6, 7], [6, 7, 8, 6], [5, 5, 6, 1]) == "FAILED"

def test2():
  assert driver([12, 6, 7, 8], [7, 8, 9, 7], [5, 6, 7, 1]) == "FAILED"

