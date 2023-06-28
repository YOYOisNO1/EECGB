from program667 import driver
def test0():
  assert driver("corner", "AaEeIiOoUu", 2) == "PASSED"

def test1():
  assert driver("valid", "AaEeIiOoUu", 2) == "PASSED"

def test2():
  assert driver("true", "AaEeIiOoUu", 2) == "PASSED"

