from program516 import driver
def test0():
  assert driver([15, 79, 25, 68, 37], [15, 25, 37, 68, 79]) == "PASSED"

def test1():
  assert driver([9, 11, 8, 7, 3, 2], [2, 3, 7, 8, 9, 11]) == "PASSED"

def test2():
  assert driver([36, 12, 24, 26, 29], [12, 24, 26, 29, 36]) == "PASSED"

