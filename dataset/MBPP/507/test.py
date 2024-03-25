from program507 import driver
def test0():
  assert driver(["red", "green", "blue", "white", "black", "orange"], ["white", "orange"], ["red", "green", "blue", "black"]) == "PASSED"

def test1():
  assert driver(["red", "green", "blue", "white", "black", "orange"], ["black", "orange"], ["red", "green", "blue", "white"]) == "PASSED"

def test2():
  assert driver(["red", "green", "blue", "white", "black", "orange"], ["blue", "white"], ["red", "green", "black", "orange"]) == "PASSED"

