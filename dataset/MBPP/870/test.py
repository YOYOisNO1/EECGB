from program870 import driver
def test0():
  assert driver([2, 4, -6, -9, 11, -12, 14, -5, 17], 48) == "PASSED"

def test1():
  assert driver([10, 15, -14, 13, -18, 12, -20], 50) == "PASSED"

def test2():
  assert driver([19, -65, 57, 39, 152, -639, 121, 44, 90, -190], 522) == "PASSED"

