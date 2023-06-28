from program584 import driver
def test0():
  assert driver("Clearly, he has no excuse for such behavior.", "0-7: Clearly") == "PASSED"

def test1():
  assert driver("Please handle the situation carefuly", "28-36: carefuly") == "PASSED"

def test2():
  assert driver("Complete the task quickly", "18-25: quickly") == "PASSED"

