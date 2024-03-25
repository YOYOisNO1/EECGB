from program788 import driver
def test0():
  assert driver(["WEB", "is"], "best", ["WEB", "is", "best"]) == "FAILED"

def test1():
  assert driver(["We", "are"], "Developers", ["We", "are", "Developers"]) == "FAILED"

def test2():
  assert driver(["Part", "is"], "Wrong", ["Part", "is", "Wrong"]) == "FAILED"

