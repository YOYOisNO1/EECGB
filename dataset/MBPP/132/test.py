from program132 import driver
def test0():
  assert driver(['e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'], "exercises") == "PASSED"

def test1():
  assert driver(['p', 'y', 't', 'h', 'o', 'n'], "python") == "PASSED"

def test2():
  assert driver(['p', 'r', 'o', 'g', 'r', 'a', 'm'], "program") == "PASSED"

