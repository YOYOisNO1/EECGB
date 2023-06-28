from program332 import driver
def test0():
  assert driver("python", {"p": 1, "y": 1, "t": 1, "h": 1, "o": 1, "n": 1}) == "PASSED"

def test1():
  assert driver("program", {"p": 1, "r": 2, "o": 1, "g": 1, "a": 1, "m": 1}) == "PASSED"

def test2():
  assert driver("language", {"l": 1, "a": 2, "n": 1, "g": 2, "u": 1, "e": 1}) == "PASSED"

