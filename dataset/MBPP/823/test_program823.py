from program823 import driver
def test0():
  assert driver("dreams for dreams makes life fun", "makes", "string doesnt start with the given substring") == "PASSED"

def test1():
  assert driver("Hi there how are you Hi alex", "Hi", "string starts with the given substring") == "PASSED"

def test2():
  assert driver("Its been a long day", "been", "string doesnt start with the given substring") == "PASSED"

