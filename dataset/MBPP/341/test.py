from program341 import driver
def test0():
  assert driver(set([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]) == "FAILED"

def test1():
  assert driver(set([6, 7, 8, 9, 10, 11]), [6, 7, 8, 9, 10, 11]) == "FAILED"

def test2():
  assert driver(set([12, 13, 14, 15, 16]), [12, 13, 14, 15, 16]) == "FAILED"

