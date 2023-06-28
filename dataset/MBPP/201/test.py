from program201 import driver
def test0():
  assert driver(["one", "one", "one"], True) == "PASSED"

def test1():
  assert driver(["one", "Two", "Three"], False) == "PASSED"

def test2():
  assert driver(["bigdata", "python", "Django"], False) == "PASSED"

