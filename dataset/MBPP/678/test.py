from program678 import driver
def test0():
  assert driver("a b c", "abc") == "PASSED"

def test1():
  assert driver("1 2 3", "123") == "PASSED"

def test2():
  assert driver(" b c", "bc") == "PASSED"

