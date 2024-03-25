from program468 import driver
def test0():
  assert driver([3, 100, 4, 5, 150, 6], 6, 45000) == "PASSED"

def test1():
  assert driver([4, 42, 55, 68, 80], 5, 50265600) == "PASSED"

def test2():
  assert driver([10, 22, 9, 33, 21, 50, 41, 60], 8, 21780000) == "PASSED"

