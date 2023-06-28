from program940 import driver
def test0():
  assert driver([12, 2, 4, 5, 2, 3], [2, 2, 3, 4, 5, 12]) == "PASSED"

def test1():
  assert driver([32, 14, 5, 6, 7, 19], [5, 6, 7, 14, 19, 32]) == "PASSED"

def test2():
  assert driver([21, 15, 29, 78, 65], [15, 21, 29, 65, 78]) == "PASSED"

