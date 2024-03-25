from program828 import driver
def test0():
  assert driver("abc!@#123", [3, 3, 3]) == "FAILED"

def test1():
  assert driver("dgsuy@#$%&1255", [5, 4, 5]) == "FAILED"

def test2():
  assert driver("fjdsif627348#%$^&", [6, 6, 5]) == "FAILED"

