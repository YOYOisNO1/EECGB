from program570 import driver
def test0():
  assert driver(["Red color", "Orange#", "Green", "Orange @", "White"], ["#", "color", "@"], ["Red", "", "Green", "Orange", "White"]) == "PASSED"

def test1():
  assert driver(["Red &", "Orange+", "Green", "Orange @", "White"], ["&", "+", "@"], ["Red", "", "Green", "Orange", "White"]) == "PASSED"

def test2():
  assert driver(["Red &", "Orange+", "Green", "Orange @", "White"], ["@"], ["Red &", "Orange+", "Green", "Orange", "White"]) == "PASSED"

