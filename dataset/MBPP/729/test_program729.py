from program729 import driver
def test0():
  assert driver([1, 2, 3], [4, 5, 6], [5, 7, 9]) == "PASSED"

def test1():
  assert driver([1, 2], [3, 4], [4, 6]) == "PASSED"

def test2():
  assert driver([10, 20], [50, 70], [60, 90]) == "PASSED"

