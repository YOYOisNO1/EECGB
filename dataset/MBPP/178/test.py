from program178 import driver
def test0():
  assert driver(["language"], "python language", "Matched!") == "PASSED"

def test1():
  assert driver(["program"], "python language", "Not Matched!") == "PASSED"

def test2():
  assert driver(["python"], "programming language", "Not Matched!") == "PASSED"

