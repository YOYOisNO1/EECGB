from program105 import driver
def test0():
  assert driver([True, False, True], 2) == "PASSED"

def test1():
  assert driver([False, False], 0) == "PASSED"

def test2():
  assert driver([True, True, True], 3) == "PASSED"

