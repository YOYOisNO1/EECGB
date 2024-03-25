from program846 import driver
def test0():
  assert driver([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000], 6, 3) == "PASSED"

def test1():
  assert driver([100, 200, 300, 400], [700, 800, 900, 1000], 4, 4) == "PASSED"

def test2():
  assert driver([5, 6, 7, 8], [4, 3, 2, 1], 4, 1) == "PASSED"

