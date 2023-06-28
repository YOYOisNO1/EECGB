from program774 import driver
def test0():
  assert driver("ankitrai326@gmail.com", "Valid Email") == "PASSED"

def test1():
  assert driver("my.ownsite@ourearth.org", "Valid Email") == "PASSED"

def test2():
  assert driver("ankitaoie326.com", "Invalid Email") == "PASSED"

