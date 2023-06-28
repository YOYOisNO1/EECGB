from program593 import driver
def test0():
  assert driver("216.08.094.196", "216.8.94.196") == "PASSED"

def test1():
  assert driver("12.01.024", "12.1.24") == "PASSED"

def test2():
  assert driver("216.08.094.0196", "216.8.94.196") == "PASSED"

