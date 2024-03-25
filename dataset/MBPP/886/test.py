from program886 import driver
def test0():
  assert driver([8, 2, 3, 0, 7], 4.0) == "PASSED"

def test1():
  assert driver([-10, -20, -30], -20.0) == "PASSED"

def test2():
  assert driver([19, 15, 18], 17.333333333333332) == "PASSED"

