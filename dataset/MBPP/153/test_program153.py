from program153 import driver
def test0():
  assert driver(5, 3, 2, [-0.3, 1.55]) == "FAILED"

def test1():
  assert driver(9, 8, 4, [-0.4444444444444444, 2.2222222222222223]) == "FAILED"

def test2():
  assert driver(2, 4, 6, [-1.0, 4.0]) == "FAILED"

