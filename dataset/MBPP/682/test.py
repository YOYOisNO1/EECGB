from program682 import driver
def test0():
  assert driver([1, 2, 3], [4, 5, 6], [4, 10, 18]) == "PASSED"

def test1():
  assert driver([1, 2], [3, 4], [3, 8]) == "PASSED"

def test2():
  assert driver([90, 120], [50, 70], [4500, 8400]) == "PASSED"

