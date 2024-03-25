from program90 import driver
def test0():
  assert driver(["python", "PHP", "bigdata"], 7) == "PASSED"

def test1():
  assert driver(["a", "ab", "abc"], 3) == "PASSED"

def test2():
  assert driver(["small", "big", "tall"], 5) == "PASSED"

