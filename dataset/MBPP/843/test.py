from program843 import driver
def test0():
  assert driver(12, [2, 7, 13, 19], 32) == "PASSED"

def test1():
  assert driver(10, [2, 7, 13, 19], 26) == "PASSED"

def test2():
  assert driver(100, [2, 7, 13, 19], 5408) == "PASSED"

