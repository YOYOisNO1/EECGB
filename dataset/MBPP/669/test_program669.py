from program669 import driver
def test0():
  assert driver("192.168.0.1", "Valid IP address") == "PASSED"

def test1():
  assert driver("110.234.52.124", "Valid IP address") == "PASSED"

def test2():
  assert driver("366.1.2.2", "Invalid IP address") == "PASSED"

