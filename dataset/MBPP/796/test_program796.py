from program796 import driver
def test0():
  assert driver({"a": 100, "b": 200, "c": 300}, 600) == "PASSED"

def test1():
  assert driver({"a": 25, "b": 18, "c": 45}, 88) == "PASSED"

def test2():
  assert driver({"a": 36, "b": 39, "c": 49}, 124) == "PASSED"

