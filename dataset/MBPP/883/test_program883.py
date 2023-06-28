from program883 import driver
def test0():
  assert driver([19, 65, 57, 39, 152, 639, 121, 44, 90, 190], 2, 4, [152, 44]) == "PASSED"

def test1():
  assert driver([1, 2, 3, 5, 7, 8, 10], 2, 5, [10]) == "PASSED"

def test2():
  assert driver([10, 15, 14, 13, 18, 12, 20], 10, 5, [10, 20]) == "PASSED"

