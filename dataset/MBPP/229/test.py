from program229 import driver
def test0():
  assert driver([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9, [-1, -3, -7, 4, 5, 6, 2, 8, 9]) == "PASSED"

def test1():
  assert driver([12, -14, -26, 13, 15], 5, [-14, -26, 12, 13, 15]) == "PASSED"

def test2():
  assert driver([10, 24, 36, -42, -39, -78, 85], 7, [-42, -39, -78, 10, 24, 36, 85]) == "PASSED"

