from program482 import driver
def test0():
  assert driver("Geeks", "Yes") == "PASSED"

def test1():
  assert driver("geeksforGeeks", "Yes") == "PASSED"

def test2():
  assert driver("geeks", "No") == "PASSED"

