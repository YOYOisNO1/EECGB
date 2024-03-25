from program273 import driver
def test0():
  assert driver([10, 4, 5], [2, 5, 18], [8, -1, -13]) == "FAILED"

def test1():
  assert driver([11, 2, 3], [24, 45, 16], [-13, -43, -13]) == "FAILED"

def test2():
  assert driver([7, 18, 9], [10, 11, 12], [-3, 7, -3]) == "FAILED"

