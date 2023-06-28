from program305 import driver
def test0():
  assert driver(["Python PHP", "Java JavaScript", "c c++"], ["Python", "PHP"]) == "FAILED"

def test1():
  assert driver(["Python Programming", "Java Programming"], ["Python", "Programming"]) == "FAILED"

def test2():
  assert driver(["Pqrst Pqr", "qrstuv"], ["Pqrst", "Pqr"]) == "FAILED"

