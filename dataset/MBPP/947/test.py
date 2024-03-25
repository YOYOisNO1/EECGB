from program947 import driver
def test0():
  assert driver(["win", "lose", "great"], 3) == "PASSED"

def test1():
  assert driver(["a", "ab", "abc"], 1) == "PASSED"

def test2():
  assert driver(["12", "12", "1234"], 2) == "PASSED"

