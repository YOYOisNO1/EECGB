from program337 import driver
def test0():
  assert driver("python.", "Found a match!") == "PASSED"

def test1():
  assert driver("python.", "Found a match!") == "PASSED"

def test2():
  assert driver("  lang  .", "Not matched!") == "PASSED"

