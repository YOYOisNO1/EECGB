from program456 import driver
def test0():
  assert driver(["Red", "Green", "Blue", "White", "Black"], ["deR", "neerG", "eulB", "etihW", "kcalB"]) == "PASSED"

def test1():
  assert driver(["john", "amal", "joel", "george"], ["nhoj", "lama", "leoj", "egroeg"]) == "PASSED"

def test2():
  assert driver(["jack", "john", "mary"], ["kcaj", "nhoj", "yram"]) == "PASSED"

