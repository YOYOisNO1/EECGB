from program569 import driver
def test0():
  assert driver([["green", "orange"], ["black", "white"], ["white", "black", "orange"]], [["green", "orange"], ["black", "white"], ["black", "orange", "white"]]) == "PASSED"

def test1():
  assert driver([["green", "orange"], ["black"], ["green", "orange"], ["white"]], [["green", "orange"], ["black"], ["green", "orange"], ["white"]]) == "PASSED"

def test2():
  assert driver([["a", "b"], ["d", "c"], ["g", "h"], ["f", "e"]], [["a", "b"], ["c", "d"], ["g", "h"], ["e", "f"]]) == "PASSED"

