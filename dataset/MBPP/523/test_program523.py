from program523 import driver
def test0():
  assert driver("python", ["String must have 1 upper case character.", "String must have 1 number.", "String length should be atleast 8."]) == "PASSED"

def test1():
  assert driver("123python", ["String must have 1 upper case character."]) == "PASSED"

def test2():
  assert driver("123Python", ["Valid string."]) == "PASSED"

