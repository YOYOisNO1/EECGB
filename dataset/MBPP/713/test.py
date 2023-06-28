from program713 import driver
def test0():
  assert driver([True, True, True, True], True) == "PASSED"

def test1():
  assert driver([True, False, True, True], False) == "PASSED"

def test2():
  assert driver([True, True, True, True], True) == "PASSED"

