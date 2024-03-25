from program571 import driver
def test0():
  assert driver([3, 5, 10, 15, 17, 12, 9], 7, 4, 62) == "PASSED"

def test1():
  assert driver([5, 15, 10, 300], 4, 12, 25) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 5, 6], 6, 6, 21) == "PASSED"

