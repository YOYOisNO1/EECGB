from program454 import driver
def test0():
  assert driver("pythonz.", "Found a match!") == "PASSED"

def test1():
  assert driver("xyz.", "Found a match!") == "PASSED"

def test2():
  assert driver("  lang  .", "Not matched!") == "PASSED"

