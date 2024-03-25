from program450 import driver
def test0():
  assert driver(["Python", "list", "exercises", "practice", "solution"], 8, ["practice", "solution"]) == "PASSED"

def test1():
  assert driver(["Python", "list", "exercises", "practice", "solution"], 6, ["Python"]) == "PASSED"

def test2():
  assert driver(["Python", "list", "exercises", "practice", "solution"], 9, ["exercises"]) == "PASSED"

