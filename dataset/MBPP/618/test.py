from program618 import driver
def test0():
  assert driver([4, 5, 6], [1, 2, 3], [4.0, 2.5, 2.0]) == "PASSED"

def test1():
  assert driver([3, 2], [1, 4], [3.0, 0.5]) == "PASSED"

def test2():
  assert driver([90, 120], [50, 70], [1.8, 1.7142857142857142]) == "PASSED"

