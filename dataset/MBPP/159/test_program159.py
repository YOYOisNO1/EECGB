from program159 import driver
def test0():
  assert driver("January", 4, "winter") == "PASSED"

def test1():
  assert driver("October", 28, "autumn") == "PASSED"

def test2():
  assert driver("June", 6, "spring") == "PASSED"

