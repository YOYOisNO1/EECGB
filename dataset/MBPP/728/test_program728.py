from program728 import driver
def test0():
  assert driver([10, 20, 30], [15, 25, 35], [25, 45, 65]) == "PASSED"

def test1():
  assert driver([1, 2, 3], [5, 6, 7], [6, 8, 10]) == "PASSED"

def test2():
  assert driver([15, 20, 30], [15, 45, 75], [30, 65, 105]) == "PASSED"

