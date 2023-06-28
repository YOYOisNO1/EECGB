from program932 import driver
def test0():
  assert driver(["Python", "Exercises", "Practice", "Solution", "Exercises"], ["Python", "Exercises", "Practice", "Solution"]) == "PASSED"

def test1():
  assert driver(["Python", "Exercises", "Practice", "Solution", "Exercises", "Java"], ["Python", "Exercises", "Practice", "Solution", "Java"]) == "PASSED"

def test2():
  assert driver(["Python", "Exercises", "Practice", "Solution", "Exercises", "C++", "C", "C++"], ["Python", "Exercises", "Practice", "Solution", "C++", "C"]) == "PASSED"

