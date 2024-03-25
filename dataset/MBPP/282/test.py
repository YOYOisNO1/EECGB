from program282 import driver
def test0():
  assert driver([1, 2, 3], [4, 5, 6], [-3, -3, -3]) == "PASSED"

def test1():
  assert driver([1, 2], [3, 4], [-2, -2]) == "PASSED"

def test2():
  assert driver([90, 120], [50, 70], [40, 50]) == "PASSED"

