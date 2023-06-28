from program643 import driver
def test0():
  assert driver("pythonzabc.", "Found a match!") == "PASSED"

def test1():
  assert driver("xyzabc.", "Found a match!") == "PASSED"

def test2():
  assert driver("  lang  .", "Not matched!") == "PASSED"

