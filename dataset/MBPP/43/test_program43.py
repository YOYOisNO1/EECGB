from program43 import driver
def test0():
  assert driver("aab_cbbbc", "Found a match!") == "PASSED"

def test1():
  assert driver("aab_Abbbc", "Not matched!") == "PASSED"

def test2():
  assert driver("Aaab_abbbc", "Not matched!") == "PASSED"

