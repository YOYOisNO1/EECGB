from program794 import driver
def test0():
  assert driver("aabbbb", "Found a match!") == "PASSED"

def test1():
  assert driver("aabAbbbc", "Not matched!") == "PASSED"

def test2():
  assert driver("accddbbjjj", "Not matched!") == "PASSED"

