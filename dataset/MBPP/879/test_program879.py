from program879 import driver
def test0():
  assert driver("aabbbbd", "Not matched!") == "PASSED"

def test1():
  assert driver("aabAbbbc", "Not matched!") == "PASSED"

def test2():
  assert driver("accddbbjjjb", "Found a match!") == "PASSED"

