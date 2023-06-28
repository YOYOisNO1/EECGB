from program340 import driver
def test0():
  assert driver([10, 20, 30, 40, 50, 60, 7], 37) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5], 6) == "PASSED"

def test2():
  assert driver([0, 1, 2, 3, 4, 5], 6) == "PASSED"

