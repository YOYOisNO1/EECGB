from program902 import driver
def test0():
  assert driver({"a": 100, "b": 200, "c": 300}, {"a": 300, "b": 200, "d": 400}, {"b": 400, "d": 400, "a": 400, "c": 300}) == "PASSED"

def test1():
  assert driver({"a": 500, "b": 700, "c": 900}, {"a": 500, "b": 600, "d": 900}, {"b": 1300, "d": 900, "a": 1000, "c": 900}) == "PASSED"

def test2():
  assert driver({"a": 900, "b": 900, "d": 900}, {"a": 900, "b": 900, "d": 900}, {"b": 1800, "d": 1800, "a": 1800}) == "PASSED"

