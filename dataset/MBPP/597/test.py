from program597 import driver
def test0():
  assert driver([2, 3, 6, 7, 9], [1, 4, 8, 10], 5, 4, 5, 6) == "PASSED"

def test1():
  assert driver([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 5, 7, 7, 256) == "PASSED"

def test2():
  assert driver([3, 4, 7, 8, 10], [2, 5, 9, 11], 5, 4, 6, 8) == "PASSED"

