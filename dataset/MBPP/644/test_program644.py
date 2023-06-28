from program644 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6], 4, [4, 3, 2, 1, 5, 6]) == "PASSED"

def test1():
  assert driver([4, 5, 6, 7], 2, [5, 4, 6, 7]) == "PASSED"

def test2():
  assert driver([9, 8, 7, 6, 5], 3, [7, 8, 9, 6, 5]) == "PASSED"

