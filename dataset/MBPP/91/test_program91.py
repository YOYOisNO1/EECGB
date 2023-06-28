from program91 import driver
def test0():
  assert driver(["red", "black", "white", "green", "orange"], "ack", True) == "PASSED"

def test1():
  assert driver(["red", "black", "white", "green", "orange"], "abc", False) == "PASSED"

def test2():
  assert driver(["red", "black", "white", "green", "orange"], "ange", True) == "PASSED"

