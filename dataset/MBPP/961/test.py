from program961 import driver
def test0():
  assert driver("MMMCMLXXXVI", 3986) == "PASSED"

def test1():
  assert driver("MMMM", 4000) == "PASSED"

def test2():
  assert driver("C", 100) == "PASSED"

