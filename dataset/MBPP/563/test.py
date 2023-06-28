from program563 import driver
def test0():
  assert driver("\"Python\", \"PHP\", \"Java\"", ["Python", "PHP", "Java"]) == "PASSED"

def test1():
  assert driver("\"python\",\"program\",\"language\"", ["python", "program", "language"]) == "PASSED"

def test2():
  assert driver("\"red\",\"blue\",\"green\",\"yellow\"", ["red", "blue", "green", "yellow"]) == "PASSED"

