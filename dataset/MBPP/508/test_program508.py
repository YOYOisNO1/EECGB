from program508 import driver
def test0():
  assert driver(["red", "green", "black", "orange"], ["red", "pink", "green", "white", "black"], True) == "PASSED"

def test1():
  assert driver(["red", "pink", "green", "white", "black"], ["white", "orange", "pink", "black"], False) == "PASSED"

def test2():
  assert driver(["red", "green", "black", "orange"], ["red", "pink", "green", "white", "black"], True) == "PASSED"

