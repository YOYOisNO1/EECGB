from program251 import driver
def test0():
  assert driver(["Red", "Green", "Black"], "c", ["c", "Red", "c", "Green", "c", "Black"]) == "PASSED"

def test1():
  assert driver(["python", "java"], "program", ["program", "python", "program", "java"]) == "PASSED"

def test2():
  assert driver(["happy", "sad"], "laugh", ["laugh", "happy", "laugh", "sad"]) == "PASSED"

