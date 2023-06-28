from program679 import driver
def test0():
  assert driver({"physics": 80, "math": 90, "chemistry": 86}, 0, "physics") == "PASSED"

def test1():
  assert driver({"python": 10, "java": 20, "C++": 30}, 2, "C++") == "PASSED"

def test2():
  assert driver({"program": 15, "computer": 45}, 1, "computer") == "PASSED"

