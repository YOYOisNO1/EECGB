from program668 import driver
def test0():
  assert driver("peep", 'e', "pep") == "PASSED"

def test1():
  assert driver("Greek", 'e', "Grek") == "PASSED"

def test2():
  assert driver("Moon", 'o', "Mon") == "PASSED"

