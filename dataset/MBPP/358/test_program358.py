from program358 import driver
def test0():
  assert driver([4, 5, 6], [1, 2, 3], [0, 1, 0]) == "PASSED"

def test1():
  assert driver([3, 2], [1, 4], [0, 2]) == "PASSED"

def test2():
  assert driver([90, 120], [50, 70], [40, 50]) == "PASSED"

