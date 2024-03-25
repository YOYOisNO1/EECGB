from program263 import driver
def test0():
  assert driver({"a": 100, "b": 200}, {"x": 300, "y": 200}, {"x": 300, "y": 200, "a": 100, "b": 200}) == "PASSED"

def test1():
  assert driver({"a": 900, "b": 900, "d": 900}, {"a": 900, "b": 900, "d": 900}, {"a": 900, "b": 900, "d": 900}) == "PASSED"

def test2():
  assert driver({"a": 10, "b": 20}, {"x": 30, "y": 40}, {"x": 30, "y": 40, "a": 10, "b": 20}) == "PASSED"

