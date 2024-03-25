from program628 import driver
def test0():
  assert driver("My Name is Dawood", "My%20Name%20is%20Dawood") == "PASSED"

def test1():
  assert driver("I am a Programmer", "I%20am%20a%20Programmer") == "PASSED"

def test2():
  assert driver("I love Coding", "I%20love%20Coding") == "PASSED"

